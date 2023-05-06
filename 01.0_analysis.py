# 01.0_analysis.py
# This program contains the analysed information gathered from the iris dataset. 
# Author: MAtthew Arthur. 


# This is the correct way, need to fix formatting of class
import pandas as pd

# Load the iris dataset
iris_df = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Group the data by class and calculate summary statistics for each group
grouped_stats = iris_df.groupby('class').describe()


# Write the summary statistics to a text file
with open('01.1_iris_summary.txt', 'w') as f:
    for c in grouped_stats.columns.levels[0]:
        f.write('Variable: ' + c + '\n')
        f.write(str(grouped_stats[c]) + '\n\n')

f.close()



# The below script only does it as a whole, not by eachvariable
'''
irisdimensions_df = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# The above line uses the pandas module to read in the file iris.data from the folder, and uses the commas to separate the elements. 
dimensions_summary_stats = irisdimensions_df.describe()

with open('01.1_iris_summary.txt', 'w') as f:
    f.write(str(dimensions_summary_stats))
'''
