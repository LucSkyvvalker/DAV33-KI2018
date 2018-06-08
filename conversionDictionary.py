# currency from https://www.xe.com/currencyconverter on 8-06-18

rice = pd.read_csv('Riceset.csv')
conversionDict = {}
for row in rice.itertuples():
    if row.cur_name not in conversionDict:
        conversionDict[row.cur_name] = input('Currency:' + row.cur_name)