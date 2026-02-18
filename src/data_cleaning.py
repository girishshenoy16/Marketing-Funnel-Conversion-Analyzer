import pandas as pd

print("Loading dataset...")

# Load full dataset (you have 32GB RAM, so this is safe)
df = pd.read_csv("data/raw/events.csv")

print("Initial Shape:", df.shape)

# Convert datetime
df["event_time"] = pd.to_datetime(df["event_time"])

# Extract useful time features
df["event_date"] = df["event_time"].dt.date
df["event_month"] = df["event_time"].dt.strftime("%Y-%m")


# Remove rows with missing price (important for revenue analysis)
df = df[df["price"] > 0]

# Optional: Remove missing brand
df["brand"] = df["brand"].fillna("Unknown")

print("After Cleaning Shape:", df.shape)

# Save cleaned version
df.to_csv("data/processed/cleaned_events.csv", index=False)

print("Data cleaning completed.")