import pandas as pd
import numpy as np

# Sample pitcher workload data
data = {
    "Date": pd.date_range(start="2024-03-01", periods=30, freq="D"),
    "Pitches_Thrown": np.random.randint(30, 110, size=30)  # Random pitch count per game
}

df = pd.DataFrame(data)

# Compute Acute Workload (Last 7 Days) & Chronic Workload (Last 28 Days)
df["AWL"] = df["Pitches_Thrown"].rolling(window=7).sum()
df["CWL"] = df["Pitches_Thrown"].rolling(window=28).mean()

# Calculate Acute:Chronic Workload Ratio (ACWR)
df["ACWR"] = df["AWL"] / df["CWL"]

# Assign Injury Risk Based on ACWR
def risk_category(acwr):
    if acwr < 0.6 or acwr > 1.5:
        return "High Risk ⚠️"
    elif 0.8 <= acwr <= 1.3:
        return "Low Risk ✅"
    else:
        return "Moderate Risk ⚠️"

df["Injury_Risk"] = df["ACWR"].apply(lambda x: risk_category(x) if pd.notna(x) else "N/A")

# Display results
import ace_tools as tools
tools.display_dataframe_to_user(name="Pitcher Workload and Injury Risk", dataframe=df)
