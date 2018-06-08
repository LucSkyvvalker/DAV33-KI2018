import pandas as pd
import math

###
# this is an example, this loop also runs for the other common commodities
###

# # import dataset, define dictionary
# ricedict = {}
# ricedata = pd.read_csv("Riceset.csv")
# # set first price, and counter
# meanprice = ricedata['mp_price'][0]
# counter = 1
# # loop over dataset, match adjacent lines.
# for i in range(1,len(ricedata)):
#     if ricedata['adm_name'][i-1] == ricedata['adm_name'][i]:
#         # if match, add price to meanprice, increment counter
#         if ricedata['cm_name'][i-1] == ricedata['cm_name'][i]:
#             meanprice = meanprice + ricedata['mp_price'][i]
#             counter += 1
#         # when no next match, make dictionary entry and reset counter and meanprice
#         else:
#             ricedict[str(ricedata['adm_name'][i-1])+'-'+str(ricedata['cm_name'][i-1])] = (meanprice/counter)
#             meanprice = ricedata['mp_price'][i]
#             counter = 1

ricedict = {}
ricedata = pd.read_csv("newRiceDataset.csv", encoding="latin-1")
meanprice = ricedata['mp_price'][0]
counter = 1

for i in range(0,len(ricedata)):
    for j in range(i, len(ricedata)):
        if ricedata['adm0_name'][i] == ricedata['adm0_name'][j]:
            if ricedata['cm_name'][i] == ricedata['cm_name'][j]:
                if ricedata['mp_year'][i] == ricedata['mp_year'][j]:
                    if ricedata['mp_month'][i] == ricedata['mp_month'][j]:
                        meanprice = meanprice + ricedata['mp_price'][i]
                        counter += 1
                        ricedata.drop(ricedata.index[j])
                        print(ricedata['adm0_name'][i], ricedata.index[j])
        else:
            ricedict[str(ricedata['adm0_name'][i])+'-'+str(ricedata['cm_name'][i])+'-'+str(ricedata['mp_month'][i])+'-'+str(ricedata['mp_year'][i])] = (meanprice/counter)
            meanprice = ricedata['mp_price'][i]
            counter = 1
            break
