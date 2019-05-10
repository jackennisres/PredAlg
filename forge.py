import pandas as pd
import numpy as np
import mglearn

X, y = mglearn.datasets.make_forge()
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First Feature")
plt.ylabel("Second Feature")
mglearn.plots.plot_knn_classification(n_neighbors=3)
