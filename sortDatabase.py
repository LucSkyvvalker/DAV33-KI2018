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


#maak een mooie staafdiagram
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
    