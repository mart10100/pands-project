#Iris dataset analysis
###pands-project
####Author: Matthew Arthur

Research for the dataset online and summary.

The Iris Plants Database was authored by multidisciplinary scientist R.A. Fisher in 1936. [It contains information](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x) regarding sepal and petal dimensions, as well as the variety of iris. The multivariate dataset contains a collection of measuremtns of sepal and petal lengths and widths of *Iris setosa*, *Iris versicolor*, and *Iris viriginica*. Despite it being published in the Annals of Eugenics it has long been used as a means to [demonstrate different capabilites of of data analysis and visualisation.](https://archive.ics.uci.edu/ml/datasets/iris) 

Need more on research

####**Outputing a summary of each variable to a single text file:**
The first requirement of the project is to create a text file containing a summary of each variable. To do this the pandas module was used, and the [`describe()` method](https://www.w3schools.com/python/pandas/ref_df_describe.asp) was used. This gives the number of occurences of each of the variables (petal and sepal length and width), their mean, standard deviation, minimium and maximum values of each of each, as well as their first, second, and third quartiles. 
While getting a summary of the data as a whole was straightforward using this method, breaking down down by class was a better option to better compare differences between the three classes of iris. The brief in the project detail file did not specify which way to do it, so I decided that summarizing by class would be the most meaningful. The [iris.names](iris.names) file found on the ICU page incudes summary statistics of the entire dataset, so not splitting out by class would be redundant. Doing it by class proved more difficult to format, with the code used to do so explained below. I have included a overall summary as well in the [01.0_analysis.py file](01.0_analysis.py), it has been commented out at the end. 

**Unreferenced script used to summarise the data by class:**
```python
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
```

**Program explained line by line:**

`import pandas as pd`
This line is straightforward, it imports the module required to create the dataframe and names it 'pd' to make it easier to reference later. 
<br>

```python
iris_df = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
```
This line is used to define the iris dataset from the iris.data file included in the folder. The dataframe variable is named 'iris_df' and it uses the pandas module to read the raw iris.data file as a CSV file (as it the data in the file is separated by commas). The 'Header' argument is listed as none, as there is no header in the iris.data file. The dataframe then names each of the columns within the iris.data file as 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', and 'class', respectively. This information was taken from the [iris.names](iris.names) file which was retrieved from the [UCI link](https://archive.ics.uci.edu/ml/datasets/iris) provided in the project brief. With the dataset now defined under the variable 'iris_df', this can now be used to summarize the data. 
<br>

```python
grouped_stats = iris_df.groupby('class').describe()
```
The dataframe just created uses the pandas built in functions `groupby()` and `describe()` to calculate the dataframe's summary statistics. The [`describe()` method](https://www.w3schools.com/python/pandas/ref_df_describe.asp), as metioned previously can output the summary statistics in one line, without the need of doing all the calculations. the [`groupby()` method](https://www.w3schools.com/python/pandas/ref_df_groupby.asp) allowed the summary statistics to be calculated by class. This information was stored in the variable `grouped_stats` as a dataframe, to be used in the next part of the program. 
<br>

```python 
with open('01.1_iris_summary.txt', 'w') as f:
```
The first line of this section  writes ('w') the grouped statistics variable `grouped_stats` as a [text file](01.1_iris_summary.txt) called `01.1_iris_summary.txt`, and assigns the letter 'f' to the file as a variable to use in the following lines (as seen in most other programs covered in the course that deal with files). 
<br>

```python
    for c in grouped_stats.columns.levels[0]:
        f.write('Variable: ' + c + '\n')
        f.write(str(grouped_stats[c]) + '\n\n')
```
This section of the program has been kept together as it is easier to explain as a block rather than line by line. A for loop is used so that the dataframe `grouped_stats` (which has already had its statistics summarized by class). [Multi-indexing](https://www.datacamp.com/tutorial/pandas-multi-index) is used to access the variable names for the for loop. It does this by using `.levels[0]` - there are two levels to the dataframe `grouped_stats`, the first level (level [0]) being the petal and sepal dimensions, and the second level being the summary statistics. As the summary file is to be broken down by each variable, the first level[0] is used (this is easier to see/understand by printing the `grouped_stats` dataframe (done in 01.1_analysis.py but commented out)). 
Within the for loop the first line writes the string ()'variable + c +'\n'), with 'c' being the the sepal and petal dimension variables. A new line break is added to move the next line of the for loop to the next line of the output summary text. 
The line `f.write(str(grouped_stats[c]) + '\n\n')` writes out the section of the `grouped_stats` dataframe that is related to `'c'` in that specific iteration of the for loop. The two line breaks are added to separate out the different iterations of the for loop, making it easier to read the final text file. 
<br>
```python 
f.close()
```
Finally, the file f (01.1_iris_summary.txt) is closed with the `close()` method. 
<br>

**Creating histograms of each variable**



**Scatter plots of variables**



**Other analyses**
