import pandas as pd
import math

###
# this is an example, this loop also runs for the other common commodities
###

# read the csv created by unit_list.py
breadData = pd.read_csv("newBreadDataset.csv", encoding="latin-1")

# create lists of unique entries in the necessary columns
countries = list(breadData['adm0_name'].unique())
commodities = list(breadData['cm_name'].unique())
years = list(breadData['mp_year'].unique())
months = list(breadData['mp_month'].unique())

# loop over the lists and set conditions
for country in countries:
    land =  breadData['adm0_name'] == country
    for commodity in commodities:
        c = breadData['cm_name'] == commodity
        for year in years:
            y = breadData['mp_year'] == year
            for month in months:
                m = breadData['mp_month'] == month
                # create a new dataframe that meets the conditions
                breadTimeStamp = breadData[land & c & y & m]
                # if the mean of mp_price is not "nan"
                if breadTimeStamp['mp_price'].mean() > 0:
                    # set meanmp_price
                    meanmp_price = float(breadTimeStamp['mp_price'].mean())
                    # add the print, to see progress
                    #print(meanmp_price)
                    # append all values to new csv
                    with open("meanBreadData.csv", "a") as fOut:
                        fOut.write(country+",")
                        fOut.write(str(meanmp_price)+",")
                        fOut.write(breadData[land]['cur_name'].unique()[0]+",")
                        fOut.write(commodity+",KG,")
                        fOut.write(str(month)+",")
                        fOut.write(str(year))
                        fOut.write("\n")

# set list of column_names
column_names = ["adm0_name", "mp_price", "cur_name", "cm_name", "um_name", "mp_month", "mp_year"]
# open the csv
with open("meanBreadData.csv", 'r+') as fIn:
    # save the current content
    content = fIn.read()
    # find top left corner
    fIn.seek(0, 0)
    # write the column_names
    for i in column_names:
        fIn.write(i + ",")
    fIn.write("\n")
    # add the content again
    fIn.write(content)
