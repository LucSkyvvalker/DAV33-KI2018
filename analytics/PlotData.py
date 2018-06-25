# import pandas en breaddata
import pandas as pd

breaddata = pd.read_csv("finalBreadDataset.csv")

breaddata

# import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure, show, output_file

# Univariate non-graphical

# Tabulation with one variate (year frequencies)
my_tab1 = pd.crosstab(index=breaddata["mp_year"], columns="count")
my_tab1

# Tabulation with one variate (country frequencies)
my_tab = pd.crosstab(index=breaddata["adm0_name"], columns=["count"])
my_tab

# Multivariate non-graphical

# Crosstabulation with two variates (country per year)
my_crosstab = pd.crosstab(index=breaddata["adm0_name"], columns=breaddata["mp_year"])
my_crosstab.index = ["Afghanistan", "Algeria", "Armenia", "Bolivia", "Congo", "Djibouti", "Gambia", "Guatemala", "Guinea", "Iraq", "Jordan", "Kenya", "Kyrgyzstan", "Lebanon", "Lesotho", "Nigeria", "State of Palestine", "Syrian Arab Republic", "Tajikistan", "Turkey", "Ukraine"]
my_crosstab.columns=["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"]
my_crosstab

# Crosstabulation with two variates (country per month)
my_crosstab1 = pd.crosstab(index=breaddata["adm0_name"], columns=breaddata["mp_month"])
my_crosstab1.index = ["Afghanistan", "Algeria", "Armenia", "Bolivia", "Congo", "Djibouti", "Gambia", "Guatemala", "Guinea", "Iraq", "Jordan", "Kenya", "Kyrgyzstan", "Lebanon", "Lesotho", "Nigeria", "State of Palestine", "Syrian Arab Republic", "Tajikistan", "Turkey", "Ukraine"]
my_crosstab1.columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
my_crosstab1

# Univariate graphical

# Histogram product price frequencies

breaddata.hist(column="mp_price", figsize=(10,10), bins=75, color="purple

# density plot product price
breaddata["mp_price"].plot(kind="density",
                      figsize=(8,8))

# density plot month

breaddata["mp_month"].plot(kind="density",
                      figsize=(8,8))

# bar plot country frequency
my_tab.plot(kind="bar",
                 figsize=(8,8))


# Multivariate graphical

# Stacked bar plot countries per year

my_crosstab.plot(kind="bar",
                 figsize=(8,8),
                 stacked=True)

# boxplot product price per country
breaddata.boxplot(column="mp_price", by="adm0_name", figsize=(30,8))

#Scatter plot product price per year (data points at the lefthand side
# to be ignored, because that is unavailable data)
breaddata.plot(kind="scatter",     # Create a scatterplot
              x="mp_price",          # Put price on the x axis
              y="mp_year",          # Put year on the y axis
              figsize=(10,10))

# Scatter plot, same as above, but flipped
breaddata.plot(kind="scatter",     # Create a scatterplot
              x="mp_price",          # Put price on the x axis
              y="mp_year",          # Put year on the y axis
              figsize=(10,10))


# Code for map
import plotly.plotly as py
import pandas as pd
import plotly as plotly

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
plotly.tools.set_credentials_file(username='ChandniBagchi', api_key='xmBVTpvtqjQTgz9kTrJW')

data = [ dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '$',
            title = 'GDP<br>Billions US$'),
      ) ]

layout = dict(
    title = '2014 Global GDP<br>Source:\
            <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
            CIA World Factbook</a>',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
py.iplot( fig, validate=False, filename='d3-world-map' )
