import pandas as pd
import math

###
# this is an example, this loop also runs for the other common commodities
###
df = pd.read_csv("FinalSugar.csv", encoding="latin-1")
data = df.loc[:, ~df.columns.str.contains('^Unnamed')]
data

eda =[data.std(),
    data.cov(),
    data.var(),
    data.kurtosis(),
    data.skew(),
    data.median(),
    data.mode(),
    data.mean(),
    data['mp_price'].min(),
    data['mp_price'].max()]
for x in eda:
    print(x)
