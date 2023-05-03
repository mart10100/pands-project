#Iris dataset analysis
###pands-project
####Author: Matthew Arthur

Research for the dataset online and summary.

The Iris Plants Database was authored by multidisciplinary scientist R.A. Fisher in 1936. [It contains information](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x) regarding sepal and petal dimensions, as well as the variety of iris. The multivariate dataset contains a collection of measuremtns of sepal and petal lengths and widths of *Iris setosa*, *Iris versicolor*, and *Iris viriginica*. Despite it being published in the Annals of Eugenics it has long been used as a means to [demonstrate different capabilites of of data analysis and visualisation.](https://archive.ics.uci.edu/ml/datasets/iris) 

Need more on research

**Outputing a summary of each variable to a single text file:**
The first requirement of the project is to create a text file containing a summary of each variable. To do this the pandas module was used, and the [`describe()` method](https://www.w3schools.com/python/pandas/ref_df_describe.asp) was used. This gives the number of occurences of each of the variables (petal and sepal length and width), their mean, standard deviation, minimium and maximum values of each of each, as well as their first, second, and third quartiles. 

