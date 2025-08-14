import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
climate_df = pd.read_csv(r"C:\Users\bolli\Desktop\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\Climate_impacts_by_country.csv")
shift_df = pd.read_csv(r"C:\Users\bolli\Desktop\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\transboundary_range_shifts.csv")
richness_df = pd.read_csv(r"C:\Users\bolli\Desktop\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\transboundary_richness.csv")

# Identify species at high risk (Decline greater than 10%)
def identify_high_risk_species(df):
    risk_threshold = -10  # More than 10% decline
    high_risk = df[(df['rcp85_both_pctChange'] <= risk_threshold)]
    
    # Sort by highest decline and select top 15
    top_15 = high_risk[['ISO3', 'rcp85_mammal_pctChange', 'rcp85_bird_pctChange', 'rcp85_both_pctChange']].sort_values(by='rcp85_both_pctChange').head(10)
    return top_15

high_risk_species = identify_high_risk_species(climate_df)
print("Top 10 Countries with Highest Species Decline under RCP 8.5:")
print(high_risk_species.to_string(index=False))

# Merge transboundary data to find affected areas
affected_areas = richness_df.merge(shift_df, on='border')
affected_areas = affected_areas[['border', 'transboundary_richness_threatened', 'rcp85_mammals', 'rcp85_birds']]

# Select top 15 transboundary regions with highest biodiversity loss
top_15_transboundary = affected_areas.sort_values(by='transboundary_richness_threatened', ascending=False).head(10)
print("\nTop 10 Affected Transboundary Areas:")
print(top_15_transboundary.to_string(index=False))

# Visualization (Horizontal Bar Plot for Species Decline)
plt.figure(figsize=(10,8))
sns.barplot(y='ISO3', x='rcp85_both_pctChange', data=high_risk_species, width=0.5, palette="Reds_r")
plt.ylabel("Country Code")
plt.xlabel("% Decline in Species Richness (RCP 8.5)")
plt.title("Top 10 Countries with Highest Species Decline under RCP 8.5 Scenario")
plt.show()
