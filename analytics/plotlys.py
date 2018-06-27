import plotly.plotly as py
import pandas as pd
import plotly as plotly


--------

df = pd.read_csv('FinalBread.csv')
sorted(df.mp_year.unique())


--------

# verander dit per jaar dat geplot moet worden
year = df["mp_year"] == 2013
dfyear = df[year]
dfyear


--------

plotly.tools.set_credentials_file(username='ChandniBagchi', api_key='xmBVTpvtqjQTgz9kTrJW')

data = [ dict(
        type = 'choropleth',
        locationmode = 'country names',
        locations = dfyear['adm0_name'],
        z = dfyear['mp_price'],
        text = dfyear['adm0_name'],
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
            title = 'USD<br>$'),
      ) ]

layout = dict(
    title = '2013 Bread Prices',
    geo = dict(
        showland = True,
        showcountry = True,
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
py.iplot( fig, validate=False, filename='d3-world-map' )
