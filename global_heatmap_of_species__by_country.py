import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Load dataset (replace with actual file path)
climate_df = pd.read_csv(r"C:\Users\bolli\Desktop\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\Climate_impacts_by_country.csv")

# Load world map manually (Download from Natural Earth and update path)
world = gpd.read_file(r"C:\Users\bolli\Desktop\ne_110m_admin_0_countries\ne_110m_admin_0_countries.shp")

# Check available columns in world dataset
print("Available columns in world dataset:", world.columns)

# Use 'current_both_SR' as the species count column
expected_species_column = "current_both_SR"

# Merge with species count data
species_count_df = climate_df[['ISO3', expected_species_column]].dropna()
world = world.merge(species_count_df, how="left", left_on="ADM0_A3", right_on="ISO3")

# Plot world heatmap
fig, ax = plt.subplots(1, 1, figsize=(12, 6))
world.boundary.plot(ax=ax, linewidth=1)
world.plot(column=expected_species_column, cmap="YlOrRd", linewidth=0.8, edgecolor="black", legend=True, ax=ax)
plt.title("Global Heatmap of Species Count by Country")
plt.show()
