# 04.0_EDA.py
# This program runs a correlation analysis of the iris dataset variables
# Author: Matthew Arthur


#https://medium.com/@szabo.bibor/how-to-create-a-seaborn-correlation-heatmap-in-python-834c0686b88e

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris_df = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Compute the correlation matrix - .iloc[] means last column (class) is not included  
correlation_matrix = iris_df.iloc[:, :-1].corr()

# heatmap creation
sns.heatmap(correlation_matrix, cmap='coolwarm', annot=True)

# Add title, save png, and show plot
plt.title('Correlation Matrix of Iris Dataset')
plt.savefig('correlation_matrix.png')
plt.show()
plt.close()
