import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
#first we have to load the datasets
climate_df = pd.read_csv(r"C:\Users\bolli\Desktop\Bio - 2\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\Climate_impacts_by_country.csv")
shift_df = pd.read_csv(r"C:\Users\bolli\Desktop\Bio - 2\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\transboundary_range_shifts.csv")
richness_df = pd.read_csv(r"C:\Users\bolli\Desktop\Bio - 2\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\transboundary_richness.csv")

# Remove leading/trailing spaces in column names
climate_df.columns = climate_df.columns.str.strip()

#In all the datasets remove the noise(unnecessary data or the empty gaps)
shift_df.columns = shift_df.columns.str.strip()
richness_df.columns = richness_df.columns.str.strip()

# Check available columns
print("Climate DataFrame Columns:", climate_df.columns)

print("Richness DataFrame Columns:", richness_df.columns)
print("Shift DataFrame Columns:", shift_df.columns)

# Ensure expected columns exist
if "border" not in richness_df.columns:
    raise KeyError("Column 'border' not found in Richness DataFrame")

if "border" not in shift_df.columns:
    raise KeyError("Column 'border' not found in Shift DataFrame")

# Merge richness_df and shift_df using "border"
merged_df = richness_df.merge(shift_df, on="border", how="inner")

# Select relevant numerical columns for correlation
corr_columns = ['transboundary_richness', 'transboundary_richness_threatened', 
                'rcp45_mammals', 'rcp85_mammals', 'rcp45_birds', 'rcp85_birds', 'barrier_species']

# Ensure selected columns exist in the merged DataFrame

missing_cols = [col for col in corr_columns if col not in merged_df.columns]
if missing_cols:
    raise KeyError(f"Missing columns in merged DataFrame: {missing_cols}")

# Compute correlation matrix
corr_matrix = merged_df[corr_columns].corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5, vmin=-1, vmax=1)

# Formatting
plt.title("Correlation Heatmap of Climate Impact and Biodiversity Metrics", fontsize=14)

plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Show plot
plt.show()
