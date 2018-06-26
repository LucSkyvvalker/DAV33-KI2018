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
#aldskfjlasdjflasjdlksadjflkjlkj
import pandas as pd
from pandas import Series,DataFrame
from bokeh.layouts import gridplot, row, column

from bokeh.io import push_notebook, show, output_notebook
from bokeh.plotting import figure

from sklearn.datasets import load_boston

%matplotlib inline

# x voor regressie
x = pd.DataFrame(rice["mp_price"])
x["africa"] = rice.africa
x["asia"] = rice.asia
x["north_america"] = rice.north_america
x["south_america"] = rice.south_america
x.columns = ["mp_price", "africa", "asia", "north_america", "south_america"]

# Target voor regressie 
y = pd.DataFrame(rice["target"])
y.columns = ['target']


# Kmeans
rice.columns = rice.iloc[0]
x = pd.DataFrame(rice.iloc[1])

model = KMeans(n_clusters=5)
model.fit(x)

model.labels_

plt.figure(figsize=(14,7))

colormap = np.array(['red', 'lime', 'black', 'yellow', 'blue'])
plt.subplot(1, 2, 2)
plt.scatter(x.mp_price, x.mp_price, c=colormap[model.labels_], s=40)
plt.title('K Mean Classification')
predY = model.labels_