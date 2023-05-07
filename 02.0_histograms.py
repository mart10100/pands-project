# 02.0_histograms.py
# This program loads the iris dataset and uses it to create histograms of each variable by class.
# Author: Matthew Arthur. 

import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset
iris_df = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Group the data by class
grouped_data = iris_df.groupby('class')

# Plot histograms for each variable, separated by class
for col in iris_df.columns[:-1]:
    plt.figure()
    for name, group in grouped_data:
        group[col].plot(kind='hist', alpha=0.5, label=name)
    plt.legend()
    plt.title(f'Histogram of {col} by Class')
    plt.xlabel(col)
    plt.savefig(f'{col}_histogram.png')
    plt.close()