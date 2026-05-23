import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "data" / "processed" / "cleaned_events.csv"

processed_path = BASE_DIR / "data" / "processed"
outputs_path = BASE_DIR / "outputs"

processed_path.mkdir(parents=True, exist_ok=True)
outputs_path.mkdir(parents=True, exist_ok=True)

print("Loading cleaned data...")
df = pd.read_csv(input_path)

# -------------------------------------------------
# PURCHASE DATA
# -------------------------------------------------
purchase_df = df[df["event_type"] == "purchase"].copy()

# -------------------------------------------------
# SUMMARY METRICS
# -------------------------------------------------
print("Calculating revenue metrics...")

total_revenue = purchase_df["price"].sum()
aov = purchase_df["price"].mean()

summary = pd.DataFrame({
    "Total Revenue": [total_revenue],
    "Average Order Value": [aov]
})

summary.to_csv(
    outputs_path / "summary_metrics.csv",
    index=False
)

# -------------------------------------------------
# BRAND REVENUE
# -------------------------------------------------
brand_revenue = (
    purchase_df.groupby("brand")["price"]
    .sum()
    .reset_index()
)

brand_revenue.to_csv(
    outputs_path / "brand_revenue.csv",
    index=False
)

# -------------------------------------------------
# MONTHLY METRICS
# -------------------------------------------------
print("Computing monthly metrics...")

monthly_metrics = (
    purchase_df.groupby("event_month")
    .agg(
        total_revenue=("price", "sum"),
        total_purchases=("event_type", "count")
    )
    .reset_index()
)

monthly_metrics.to_csv(
    processed_path / "monthly_metrics.csv",
    index=False
)

print("✅ Monthly metrics saved.")

# -------------------------------------------------
# CATEGORY SUMMARY
# -------------------------------------------------
print("Computing category conversion summary...")

category_summary = pd.crosstab(
    df["category_code"],
    df["event_type"]
).fillna(0)

category_summary["conversion_rate"] = (
    category_summary.get("purchase", 0)
    / category_summary.get("view", 1)
) * 100

category_summary = category_summary.reset_index()

category_summary.to_csv(
    processed_path / "category_summary.csv",
    index=False
)

print("✅ Category summary saved.")

# -------------------------------------------------
# COHORT TABLE
# -------------------------------------------------
print("Computing cohort retention table...")

if purchase_df.empty:

    print("⚠ No purchase data found.")

    empty_df = pd.DataFrame()
    empty_df.to_csv(
        processed_path / "cohort_table.csv"
    )

else:

    purchase_df["event_time"] = pd.to_datetime(
        purchase_df["event_time"],
        errors="coerce"
    )

    purchase_df = purchase_df.dropna(
        subset=["event_time"]
    )

    purchase_df["purchase_month"] = (
        purchase_df["event_time"]
        .dt.to_period("M")
        .dt.to_timestamp()
    )

    cohort = purchase_df.groupby("user_id")[
        "purchase_month"
    ].min()

    purchase_df = purchase_df.merge(
        cohort.rename("cohort_month"),
        on="user_id"
    )

    purchase_df["cohort_index"] = (
        (
            purchase_df["purchase_month"].dt.year
            - purchase_df["cohort_month"].dt.year
        ) * 12
        +
        (
            purchase_df["purchase_month"].dt.month
            - purchase_df["cohort_month"].dt.month
        )
    )

    cohort_table = (
        purchase_df.groupby(
            ["cohort_month", "cohort_index"]
        )["user_id"]
        .nunique()
        .unstack(fill_value=0)
    )

    if cohort_table.shape[1] > 0:

        cohort_table = (
            cohort_table.divide(
                cohort_table.iloc[:, 0],
                axis=0
            ) * 100
        )

    cohort_table.index = (
        cohort_table.index.strftime("%Y-%m")
    )

    cohort_table.columns = (
        cohort_table.columns.astype(str)
    )

    cohort_table.to_csv(
        processed_path / "cohort_table.csv"
    )

    print("✅ Cohort table saved.")

print("🎉 Metrics engineering completed successfully.")