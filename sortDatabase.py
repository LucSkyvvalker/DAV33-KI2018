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
    