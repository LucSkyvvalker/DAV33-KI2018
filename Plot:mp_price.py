import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading dataframes
brea = pd.read_csv("FinalBread.csv", encoding='latin-1', low_memory=False, sep=",") 
whea = pd.read_csv("FinalWheat.csv", encoding='latin-1', low_memory=False, sep=",")
ric = pd.read_csv("FinalRice.csv", encoding='latin-1', low_memory=False, sep=",") 
sorg = pd.read_csv("FinalSorghum.csv", encoding='latin-1', low_memory=False, sep=",") 
mill = pd.read_csv("FinalMillet.csv", encoding='latin-1', low_memory=False, sep=",") 
maiz = pd.read_csv("FinalMaize.csv", encoding='latin-1', low_memory=False, sep=",") 
sug = pd.read_csv("FinalSugar.csv", encoding='latin-1', low_memory=False, sep=",") 

# cleaning dataframes of unnamed columns
bread = brea.loc[:, ~brea.columns.str.contains('^Unnamed')]
wheat = whea.loc[:, ~whea.columns.str.contains('^Unnamed')]
rice = ric.loc[:, ~ric.columns.str.contains('^Unnamed')]
sorghum = sorg.loc[:, ~sorg.columns.str.contains('^Unnamed')]
millet = mill.loc[:, ~mill.columns.str.contains('^Unnamed')]
maize = maiz.loc[:, ~maiz.columns.str.contains('^Unnamed')]
sugar = sug.loc[:, ~sug.columns.str.contains('^Unnamed')]

# hardcoded month function
def asdf(month):
    if month == 1:
        month = "01"
    elif month == 2:
        month = "02"
    elif month == 3:
        month = "03"
    elif month == 4:
        month = "04"
    elif month == 5:
        month = "05"
    elif month == 6:
        month = "06"
    elif month == 7:
        month = "07"
    elif month == 8:
        month = "08"
    elif month == 9:
        month = "09"
    elif month == 10:
        month = "10"
    elif month == 11:
        month = "11"
    elif month == 12:
        month = "12"
    return month

# correct the date for analysis
for row in bread.itertuples():
     bread.at[row.Index, "date"] = str(bread.loc[row.Index, "mp_year"]) +'-'+ asdf(bread.loc[row.Index, "mp_month"]) +'-'+ "01"
for row in wheat.itertuples():
     wheat.at[row.Index, "date"] = str(wheat.loc[row.Index, "mp_year"]) +'-'+ asdf(wheat.loc[row.Index, "mp_month"]) +'-'+ "01"
for row in rice.itertuples():
     rice.at[row.Index, "date"] = str(rice.loc[row.Index, "mp_year"]) +'-' + asdf(rice.loc[row.Index, "mp_month"]) +'-'+ "01"
for row in sorghum.itertuples():
     sorghum.at[row.Index, "date"] = str(sorghum.loc[row.Index, "mp_year"]) +'-' + asdf(sorghum.loc[row.Index, "mp_month"]) +'-'+ "01"
for row in millet.itertuples():
    millet.at[row.Index, "date"] = str(millet.loc[row.Index, "mp_year"]) +'-' + asdf(millet.loc[row.Index, "mp_month"]) +'-'+ "01"
for row in maize.itertuples():
    maize.at[row.Index, "date"] = str(maize.loc[row.Index, "mp_year"]) +'-' + asdf(maize.loc[row.Index, "mp_month"]) +'-'+ "01"
for row in sugar.itertuples():
    sugar.at[row.Index, "date"] = str(sugar.loc[row.Index, "mp_year"]) +'-' + asdf(sugar.loc[row.Index, "mp_month"]) +'-'+ "01"

        
        
bread['date'] = bread['date'].astype('datetime64[ns]')
wheat['date'] = wheat['date'].astype('datetime64[ns]')
rice['date'] = rice['date'].astype('datetime64[ns]')
sorghum['date'] = sorghum['date'].astype('datetime64[ns]')
millet['date'] = millet['date'].astype('datetime64[ns]')
maize['date'] = maize['date'].astype('datetime64[ns]')
sugar['date'] = sugar['date'].astype('datetime64[ns]')

# initialize variables 
frames = [bread, wheat, rice, millet, sugar, sorghum, maize]
data = pd.concat(frames)
countries = list(data['adm0_name'].unique())

# loop over countries and plot data based on country name (cm_name) 
for country in countries:
    land = data['adm0_name'] == country
    foo = data[land]
    fig, ax = plt.subplots(figsize=(15,7))
    foo.groupby(['date','cm_name']).sum()['mp_price'].unstack().plot(ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.title(country)