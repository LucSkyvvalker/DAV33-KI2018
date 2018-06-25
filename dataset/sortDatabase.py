# SORTEER OP DATUM, het aantal colommen in de lege dataframes moeten misschien worden aangepast aangezien "Unnamed: 7"
# er nu ook tussen staat 
def sortbydate(dataframe):
    sortedlist = pd.DataFrame(columns=["adm0_name", "mp_price", "cur_name", "cm_name", "um_name", "mp_month", "mp_year", "Unnamed: 7"])
    for country in dataframe.adm0_name.unique():
        iscountry = dataframe.adm0_name == country
        sortedlist = sortedlist.append(dataframe[iscountry].sort_values("mp_year"))
    newsortedlist = pd.DataFrame(columns=["adm0_name", "mp_price", "cur_name", "cm_name", "um_name", "mp_month", "mp_year", "Unnamed: 7"])

    for country in sortedlist.adm0_name.unique():
        iscountry = sortedlist.adm0_name == country
        for year in sortedlist[iscountry].mp_year.unique():
            isyear = sortedlist[iscountry].mp_year == year
            newsortedlist = newsortedlist.append(sortedlist[isyear&iscountry].sort_values("mp_month"))
    newsortedlist = newsortedlist.reset_index(drop=True)
    return newsortedlist

list = sortbydate(rice)
print(list.to_string())

#Steeds vorige code herhalen om alle datasets te sorteren
rice = pd.read_csv("finalRiceDataset.csv", encoding='latin-1', low_memory=False, sep=",") 
fixedrice = sortbydate(rice)
fixedrice.to_csv(path_or_buf="sortedFinalFixedRice.csv")

wheat = pd.read_csv("finalWheatDataset.csv", encoding='latin-1', low_memory=False, sep=",") 
fixedwheat = sortbydate(wheat)
fixedwheat.to_csv(path_or_buf="sortedFinalFixedWheat.csv")

bread = pd.read_csv("finalBreadDataset.csv", encoding='latin-1', low_memory=False, sep=",") 
fixedbread = sortbydate(bread)
fixedbread.to_csv(path_or_buf="sortedFinalFixedBread.csv")

maize = pd.read_csv("finalMaizeDataset.csv", encoding='latin-1', low_memory=False, sep=",") 
fixedmaize = sortbydate(maize)
fixedmaize.to_csv(path_or_buf="sortedFinalFixedMaize.csv")

millet = pd.read_csv("finalMilletDataset.csv", encoding='latin-1', low_memory=False, sep=",") 
fixedmillet = sortbydate(millet)
fixedmillet.to_csv(path_or_buf="sortedFinalFixedMillet.csv")

sorghum = pd.read_csv("finalSorghumDataset.csv", encoding='latin-1', low_memory=False, sep=",") 
fixedsorghum = sortbydate(sorghum)
fixedsorghum.to_csv(path_or_buf="sortedFinalFixedSorghum.csv")

sugar = pd.read_csv("finalSugarDataset.csv", encoding='latin-1', low_memory=False, sep=",") 
fixedsugar = sortbydate(sugar)
fixedsugar.to_csv(path_or_buf="sortedFinalFixedSugar.csv")

#maak een mooie staafdiagram 
'''
fixedrice = sortbydate(rice)

averages = {}
for country in fixedrice.adm0_name:
    iscountry = fixedrice.adm0_name == country
    if country not in averages:
        averages[country] = fixedrice[iscountry]["mp_price"].mean()
print([*averages])

output_file("bars.html")

cc = [*averages]

keys = averages.keys()
values = []
for key in keys:
    values.append(averages[key])

pp = figure(x_range=cc, plot_height=500, plot_width=5000, title="Gemiddelde prijs van suiker",
           toolbar_location=None, tools="")

pp.vbar(x=cc, top=values, width=0.9)

pp.xgrid.grid_line_color = None
pp.y_range.start = 0

show(pp)
    '''