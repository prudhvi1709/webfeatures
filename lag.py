import pandas as pd
import itertools
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("Delays.csv")

# Handle missing values (if browser has not released the feature)
df.fillna(-1, inplace=True)  # Mark unreleased features with -1

# Extract unique browsers
browsers = set(df["First Browser"]).union(set(df["Following Browser"]))

# Create a DataFrame to store pairwise comparisons
pairwise_data = []

# Iterate through features
for _, row in df.iterrows():
    first_browser = row["First Browser"]
    following_browser = row["Following Browser"]
    delay = row["Delay (Days)"]

    if first_browser != following_browser:
        if delay != -1:  # Only consider cases where delay exists
            pairwise_data.append((first_browser, following_browser, delay))

# Convert to DataFrame
pairwise_df = pd.DataFrame(pairwise_data, columns=["Lead", "Follow", "Delay"])

# Aggregate Mean Delays
mean_delays = pairwise_df.groupby(["Lead", "Follow"])["Delay"].mean().unstack()
mean_delays.to_excel("browser_delyas_code.xlsx")

# Plot Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(mean_delays, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Average Delay Between Browser Releases")
plt.show()

# Boxplot of Delay Distributions
plt.figure(figsize=(12, 6))
sns.boxplot(data=pairwise_df, x="Lead", y="Delay")
plt.xticks(rotation=90)
plt.title("Distribution of Delay by Leading Browser")
plt.show()
