import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd


# Check available columns
print("Available columns in climate_df:", climate_df.columns)

# Sort and select last 10 countries with lowest biodiversity loss
last_10_countries = climate_df[['ISO3', 'rcp85_both_pctChange']].sort_values(by='rcp85_both_pctChange', ascending=False).tail(10)

# Bar plot for last 10 countries
plt.figure(figsize=(10, 6))
sns.barplot(y='ISO3', x='rcp85_both_pctChange', data=last_10_countries, palette="Greens_r")
plt.xlabel("% Decline in Species Richness (RCP 8.5)")
plt.ylabel("Country Code")
plt.title("Last 10 Countries with Lowest Biodiversity Loss")
plt.grid(axis="x")
plt.show()
