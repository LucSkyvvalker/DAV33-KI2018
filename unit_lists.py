import pandas as pd
import math

###
# this is an example, this loop also runs for the other common commodities
###

# loop over the dataset and convert prices with convert_prices()
ricedata = pd.read_csv("Riceset.csv", encoding="latin-1")

for i in range(len(ricedata)):
    ricedata.at[i, 'mp_price'] = convert_prices(ricedata['mp_price'][i], ricedata['um_name'][i])
    ricedata.at[i, 'um_name'] = 'KG'
ricedata.to_csv(path_or_buf="newRiceDataset.csv")

###
# a massive function that checks the given measurement trough if-elif statements
# and converts the price accordingly
###
def convert_prices(price, measurement):
    if measurement == 'KG':
        new_price = price
    elif measurement == 'Pound':
        new_price = price/0.45359237
    elif measurement == '90 KG':
        new_price = price/90
    elif measurement == 'MT':
        new_price = price/1000000000
    elif measurement == '45 KG':
        new_price = price/45
    elif measurement == '500 KG':
        new_price = price/500
    elif measurement == 'Marmite':
        new_price = price/2.72155422
    elif measurement == '100 KG':
        new_price = price100
    elif measurement == '25 KG':
        new_price = price/25
    elif measurement == 'Unit':
        new_price = price/0.6
    elif measurement == '500 G':
        new_price = price/0.5
    elif measurement == '400 G':
        new_price = price/0.4
    elif measurement == '150 G':
        new_price = price/0.15
    elif measurement == 'Loaf':
        new_price = price/0.6
    elif measurement == '1.5 KG':
        new_price = price/1.5
    elif measurement == '12.5 KG':
        new_price = price/12.5
    elif measurement == '50 KG':
        new_price = price/50
    elif measurement == 'Pound':
        new_price = price/0.45359237
    elif measurement == '750 KG':
        new_price = price/750
    elif measurement == 'Cuartilla':
        new_price = price/2.875575
    elif measurement == '125 G':
        new_price = price/0.125
    elif measurement == '11.5 KG':
        new_price = price/11.5
    elif measurement == '380 G':
        new_price = price/0.380
    elif measurement == '385 G':
        new_price = price/0.385
    elif measurement == '185 G':
        new_price = price/0.185
    elif measurement == '85 G':
        new_price = price/0.085
    elif measurement == '91 KG':
        new_price = price/91
    elif measurement == '650 G':
        new_price = price/0.650
    elif measurement == '115 G':
        new_price = price/0.115
    elif measurement == '350 G':
        new_price = price/0.350
    elif measurement == '1.8 KG':
        new_price = price/1.8
    elif measurement == '2 KG':
        new_price = price/2
    elif measurement == '300 G':
        new_price = price/0.300
    elif measurement == '160 G':
        new_price = price/0.160
    elif measurement == '5 KG':
        new_price = price/5
    elif measurement == '200 G':
        new_price = price/0.2
    elif measurement == '10 KG':
        new_price = price/10
    elif measurement == '750 G':
        new_price = price/0.75
    elif measurement == '12 KG':
        new_price = price/12
    elif measurement == '18 KG':
        new_price = price/18
    elif measurement == '60 KG':
        new_price = price/60
    elif measurement == '3 KG':
        new_price = price/3
    elif measurement == '3.5 KG':
        new_price = price/3.5
    return(round(new_price, 2))
