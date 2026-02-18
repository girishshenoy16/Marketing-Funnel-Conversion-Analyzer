import pandas as pd

print("Loading cleaned data...")
df = pd.read_csv("data/processed/cleaned_events.csv")

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