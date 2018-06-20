rice = rice[rice.mp_year == 2016]
rice = rice[["adm0_name", "mp_price", "mp_month"]]
rice = rice.transpose()
rice

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm
import pandas as pd
import numpy as np
import numpy as np

import pandas as pd
from pandas import Series,DataFrame
from bokeh.layouts import gridplot, row, column

from bokeh.io import push_notebook, show, output_notebook
from bokeh.plotting import figure

from sklearn.datasets import load_boston

%matplotlib inline

rice.columns = rice.iloc[0]
x = pd.DataFrame(rice.iloc[1])

# K Means Cluster
model = KMeans(n_clusters=5)
model.fit(x)

# This is what KMeans thought
model.labels_

# View the results
# Set the size of the plot
plt.figure(figsize=(14,7))
 
# Create a colormap
colormap = np.array(['red', 'lime', 'black', 'yellow', 'blue'])
 
# Plot the Models Classifications
plt.subplot(1, 2, 2)
plt.scatter(x.mp_price, x.mp_price, c=colormap[model.labels_], s=40)
plt.title('K Mean Classification')
predY = model.labels_