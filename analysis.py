import pandas as pd
from itertools import combinations

# Sample DataFrame
# Replace this with actual CSV reading if needed (e.g., df = pd.read_csv('data.csv'))
data= pd.read_csv('Delays.csv')
df = pd.DataFrame(data)

# List of unique browsers
browsers = set(df['First Browser']).union(set(df['Following Browser']))

# Dictionary to store delays
browser_delays = {pair: [] for pair in combinations(browsers, 2)}

# Process each feature
for feature, group in df.groupby('Feature'):
    first_releases = group[['First Browser', 'Following Browser', 'Delay (Days)']]

    # Identify the first browser to release the feature
    first_browser = first_releases.iloc[0]['First Browser']

    # Compare delays for all following browsers
    for _, row in first_releases.iterrows():
        following_browser = row['Following Browser']
        delay = row['Delay (Days)']
        pair = tuple(sorted([first_browser, following_browser]))  # Sort to maintain consistency
        if pair in browser_delays:
            browser_delays[pair].append(delay)

# Compute average delays
average_delays = {pair: sum(delays) / len(delays) if delays else None for pair, delays in browser_delays.items()}

# Convert results into a DataFrame
result_df = pd.DataFrame([(pair[0], pair[1], avg_delay) for pair, avg_delay in average_delays.items() if avg_delay is not None],
                         columns=['First Browser', 'Following Browser', 'Average Delay (Days)'])

# Save results to a CSV file
result_df.to_csv('average_delays.csv', index=False)  # Specify the filename and set index to False

# Display results
print(result_df)

