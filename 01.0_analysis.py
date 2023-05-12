# 01.0_analysis.py
# This program contains the analysed information gathered from the iris dataset. 
# Author: MAtthew Arthur. 


# This is the correct way, need to fix formatting of class
import pandas as pd

# Load the iris dataset
iris_df = pd.read_csv('iris.data', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Group the data by class and calculate summary statistics for each group
grouped_stats = iris_df.groupby('class').describe()

#printed the grouped_stats df to understand exactly where the variables and stats were showing up, and to get an idea of their level in terms of the multi-indexing within the dataframe. 
#print(grouped_stats)

# Write the summary statistics to a text file
with open('01.1_iris_summary.txt', 'w') as f:
    for c in grouped_stats.columns.levels[0]:
        f.write('Variable: ' + c + '\n')
        f.write(str(grouped_stats[c]) + '\n\n')

f.close()



# The below script only does it as a whole, not by eachvariable

#irisdimensions_df = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# The above line uses the pandas module to read in the file iris.data from the folder, and uses the commas to separate the elements. 
