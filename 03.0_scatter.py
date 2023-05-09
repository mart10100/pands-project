# 03.0_scatter.py

import pandas as pd
import matplotlib.pyplot as plt

iris_df = pd.read_csv('iris.data', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

variable_xys = [('sepal_length', 'sepal_width'), ('petal_length', 'petal_width')]

for x_val, y_val in variable_xys:
    plt.scatter(iris_df[x_val], iris_df[y_val])
    plt.legend(title = 'Species', c = colours)
    plt.xlabel(f'{x_val} (cm)')
    plt.xlabel(f'{y_val} (cm)')
    plt.title(f'Scatter plot of {y_val} vs {x_val}')
    plt.show()

    plt.scatter(iris_df[x_val], iris_df[y_val], c=[colors[c] for c in iris_df['class']])