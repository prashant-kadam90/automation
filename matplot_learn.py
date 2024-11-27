#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:49:37 2024

@author: prashantkadam
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skewnorm, kurtosis

# Set up the figure and axes
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Normal Distribution
data_normal = np.random.normal(loc=0, scale=1, size=1000)
sns.histplot(data_normal, kde=True, ax=axes[0])
axes[0].set_title("Normal Distribution")
axes[0].set_xlim(-5, 5)

# Right-Skewed Distribution
data_skewed = skewnorm.rvs(a=10, loc=0, scale=1, size=1000)
sns.histplot(data_skewed, kde=True, ax=axes[1])
axes[1].set_title("Right-Skewed Distribution")
axes[1].set_xlim(-5, 15)

# Heavy-Tailed Distribution (e.g., Laplace distribution)
data_heavy_tailed = np.random.laplace(loc=0, scale=1, size=1000)
sns.histplot(data_heavy_tailed, kde=True, ax=axes[2])
axes[2].set_title("Heavy-Tailed Distribution (Laplace)")
axes[2].set_xlim(-5, 5)

# Show plots
plt.tight_layout()
plt.show()

# Calculate and print the values for the distributions
print("Normal Distribution:")
print(f"Mean: {np.mean(data_normal):.2f}, Variance: {np.var(data_normal):.2f}, Skewness: {np.mean(data_normal):.2f}, Kurtosis: {kurtosis(data_normal):.2f}")

print("\nRight-Skewed Distribution:")
print(f"Mean: {np.mean(data_skewed):.2f}, Variance: {np.var(data_skewed):.2f}, Skewness: {np.mean(data_skewed):.2f}, Kurtosis: {kurtosis(data_skewed):.2f}")

print("\nHeavy-Tailed Distribution:")
print(f"Mean: {np.mean(data_heavy_tailed):.2f}, Variance: {np.var(data_heavy_tailed):.2f}, Skewness: {np.mean(data_heavy_tailed):.2f}, Kurtosis: {kurtosis(data_heavy_tailed):.2f}")
