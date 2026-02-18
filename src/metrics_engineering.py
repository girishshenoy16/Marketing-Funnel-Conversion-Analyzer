import pandas as pd

print("Loading cleaned data...")
df = pd.read_csv("data/processed/cleaned_events.csv")

print("Calculating revenue metrics...")

# Revenue only from purchase events
purchase_df = df[df["event_type"] == "purchase"]

# Total revenue
total_revenue = purchase_df["price"].sum()

# Revenue by brand
brand_revenue = purchase_df.groupby("brand")["price"].sum().reset_index()

brand_revenue.to_csv("outputs/brand_revenue.csv", index=False)

# Average Order Value
aov = purchase_df["price"].mean()

summary = pd.DataFrame({
    "Total Revenue": [total_revenue],
    "Average Order Value": [aov]
})

summary.to_csv("outputs/summary_metrics.csv", index=False)

# -----------------------------
# MONTHLY EXECUTIVE METRICS
# -----------------------------
monthly_metrics = (
    df.groupby("event_month")
    .agg(
        total_events=("event_type", "count"),
        total_revenue=("price", lambda x: x[df["event_type"] == "purchase"].sum())
    )
    .reset_index()
)

monthly_metrics.to_csv("data/processed/monthly_metrics.csv", index=False)

print("Metrics calculated successfully.")