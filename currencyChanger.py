rice = pd.read_csv('Riceset.csv')
# rice

# variabelen
currency = 0.0140037
currencyName = 'AFN'

# loop per rij 
for row in rice.itertuples():
    if row.cur_name == currencyName:
        # calculate new value
        new_price = row.mp_price * currency
        # update values
        rice.at[row.Index, 'mp_price'] = new_price
        rice.at[row.Index, 'cur_name'] = 'USD'