# 02.0_histograms.py
# This program loads the iris dataset and uses it to create histograms of each variable by class.
# Author: Matthew Arthur. 

import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset - same as in the analysis.py file (won't be duplicated in final program)
iris_df = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Group the data by class (also won't be duplicated in final program)
grouped_stats = iris_df.groupby('class')

# Printed the grouped_stats just to get a visual understanding of what the indexing looks like
#print(grouped_stats.describe())

# Plot histograms for each variable, separated by class
for col in iris_df.columns[:-1]:
    for name, group in grouped_stats:
        group[col].plot(kind='hist', alpha=0.5)
    plt.legend()
    plt.title(f'{col} Frequency vs Measurement by Class')
    plt.xlabel(f'{col} (mm)')
    plt.savefig(f'{col}_histogram.png')
    plt.close()
'''
# Ungrouped histograms:
for col in iris_df.columns[:-1]:
    plt.figure()
    iris_df[col].plot(kind='hist', alpha=0.5)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.savefig(f'ungrouped_{col}_histogram.png')
    plt.close()
'''