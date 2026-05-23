import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "data" / "processed" / "cleaned_events.csv"
output_path = BASE_DIR / "data" / "processed" / "session_summary.csv"

print("Loading cleaned data...")
df = pd.read_csv(input_path)

print("Creating session-level funnel summary...")

# Aggregate session-level funnel logic
session_summary = df.groupby("user_session").agg(
    user_id=("user_id", "first"),
    event_month=("event_month", "first"),
    has_view=("event_type", lambda x: (x == "view").any()),
    has_cart=("event_type", lambda x: (x == "cart").any()),
    has_purchase=("event_type", lambda x: (x == "purchase").any())
).reset_index()

# Save
session_summary.to_csv(output_path, index=False)

print("Session summary saved successfully.")

print("Creating session-level funnel...")

# Aggregate events at session level
session_funnel = df.groupby("user_session")["event_type"] \
    .value_counts().unstack().fillna(0)

# Create funnel flags
session_funnel["view_flag"] = session_funnel.get("view", 0) > 0
session_funnel["cart_flag"] = session_funnel.get("cart", 0) > 0
session_funnel["purchase_flag"] = session_funnel.get("purchase", 0) > 0

# Save
session_funnel.to_csv("data/processed/session_funnel.csv")

print("Funnel engineering completed.")