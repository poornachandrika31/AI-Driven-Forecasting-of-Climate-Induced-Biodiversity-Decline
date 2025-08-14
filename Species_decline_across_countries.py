import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
climate_df = pd.read_csv(r"C:\Users\bolli\Desktop\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\Climate_impacts_by_country.csv")
shift_df = pd.read_csv(r"C:\Users\bolli\Desktop\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\transboundary_range_shifts.csv")
richness_df = pd.read_csv(r"C:\Users\bolli\Desktop\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\transboundary_richness.csv")
# Histogram of percentage decline in species richness
plt.figure(figsize=(10, 6))

# Identify species at high risk (Decline greater than 10%)
def identify_high_risk_species(df):
    risk_threshold = -10  # More than 10% decline
    high_risk = df[(df['rcp85_both_pctChange'] <= risk_threshold)]
    
    # Sort by highest decline and select top 15
    top_15 = high_risk[['ISO3', 'rcp85_mammal_pctChange', 'rcp85_bird_pctChange', 'rcp85_both_pctChange']].sort_values(by='rcp85_both_pctChange').head(10)
    return top_15

high_risk_species = identify_high_risk_species(climate_df)
sns.histplot(high_risk_species['rcp85_both_pctChange'], bins=15, kde=True, color='blue')
plt.xlabel("% Decline in Species Richness (RCP 8.5)")
plt.ylabel("Frequency of Countries")
plt.title("Distribution of Species Decline Across Countries")
plt.grid()
plt.show()
