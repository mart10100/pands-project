# 03.0_scatter.py
# Scatter plots output to show iris dataset lengths vs width, coloured by class. 
# Author: Matthew Arthur. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris_df = pd.read_csv('iris.data', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
''' 
This is a bit clunky and inefficient - can a for loop be used? Probably with some heawrecking... 

sns.scatterplot(data = iris_df, x =  'sepal_length', y =  'sepal_width', hue = 'class') -- https://www.geeksforgeeks.org/create-a-scatter-plot-using-sepal-length-and-petal_width-to-separate-the-species-classes-using-scikit-learn/
plt.title('Sepal Length vs Sepal Width')
plt.show()
sns.scatterplot(data = iris_df, x = 'petal_length', y = 'petal_width', hue = 'class')
plt.title('Petal Length vs Petal Width')
plt.show()
'''
# Back to figuring out another for loop

# Define x and y variables
# lengths = ['sepal_length', 'petal_length']-- These did not work for providing with variables, as the for loop output petal length vs sepal width, and sepal length vs petal width in addition to petal l v w and sepal l v w. 
# widths = ['sepal_width', 'petal_width'] -- can try a list of tuples

dimensions = [('sepal_length', 'sepal_width'), ('petal_length', 'petal_width')]

# Create scatterplots for all combinations of x and y variables
for length, width in dimensions:
    sns.scatterplot(data = iris_df, x = length, y = width, hue = 'class')
    plt.xlabel(f'{length} (cm)')
    plt.ylabel(f'{width} (cm)')
    plt.title(f'{length} vs {width}')
    plt.legend()
    plt.savefig(f'scatter_{length}_vs_{width}.png')
    plt.show()