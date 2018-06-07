import pandas as pd
import math

###
# this is an example, this loop also runs for the other common commodities
###

# import dataset, define dictionary
ricedict = {}
ricedata = pd.read_csv("Riceset.csv")
# set first price, and counter
meanprice = ricedata['mp_price'][0]
counter = 1
# loop over dataset, match adjacent lines.
for i in range(1,len(ricedata)):
    if ricedata['adm_name'][i-1] == ricedata['adm_name'][i]:
        # if match, add price to meanprice, increment counter
        if ricedata['cm_name'][i-1] == ricedata['cm_name'][i]:
            meanprice = meanprice + ricedata['mp_price'][i]
            counter += 1
        # when no next match, make dictionary entry and reset counter and meanprice
        else:
            ricedict[str(ricedata['adm_name'][i-1])+'-'+str(ricedata['cm_name'][i-1])] = (meanprice/counter)
            meanprice = ricedata['mp_price'][i]
            counter = 1
