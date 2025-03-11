import numpy as np
from scipy.stats import chi2_contingency

# Your observed frequency table
observed = np.array([
    [26, 14, 5, 37, 6, 7, 129, 0, 25, 22, 100, 287, 272, 7, 305, 259],
    [564, 313, 18, 49, 664, 611, 17, 47, 25, 593, 449, 105, 69, 9, 300, 68],
    [68, 561, 39, 642, 12, 14, 4, 3, 0, 180, 156, 112, 119, 245, 208, 118],
    [269, 24, 35, 105, 11, 6, 95, 0, 0, 134, 153, 68, 38, 87, 12, 26],
    [21, 11, 0, 106, 0, 2, 84, 1, 0, 27, 131, 198, 162, 9, 198, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 9, 402, 0, 9, 0]
])

# Perform chi-square test
chi2_stat, p, dof, expected = chi2_contingency(observed)

# Normalize expected frequencies to match the sum of observed frequencies
expected *= observed.sum() / expected.sum()

# Run the test again after fixing the mismatch
chi2_stat, p, dof, expected = chi2_contingency(observed)

print(f"Chi-square statistic: {chi2_stat}")
print(f"P-value: {p}")
