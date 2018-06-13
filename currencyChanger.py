import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('meanRiceData.csv')

conversionDict = {'AFN': '0.0140151', 'DZD': '0.00855952', 'AMD': '0.00206902',
    'BDT': '0.0118332', 'XOF': '0.00179909', 'BTN': '0.0148341', 'BOB': '0.144752',
    'BIF': '0.000560449', 'KHR': '0.000245134', 'XAF': '0.00179932', 'CVE': '0.0107035',
    'COP': '0.000351189', 'USD': '1', 'CDF': '0.000623955', 'DJF': '0.00562280',
    'ETB': '0.0362410', 'GMD': '0.0211896', 'GHS': '0.211724', 'GTQ': '0.133725',
    'GNF': '0.000110474', 'HTG': '0.0154506', 'INR': '0.0147745', 'IDR': '0.0000714730',
    'IRR': '0.0000237128', 'IQD': '0.000840403', 'JOD': '1.41044', 'KGS': '0.0146210',
    'LAK': '0.000119254', 'LBP': '0.000663350', 'LRD': '0.00721177', 'MGA': '0.000296944',
    'MWK': '0.00133360', 'MRO': '0.00281186', 'MZN': '0.0168489', 'MMK': '0.000738016',
    'NPR': '0.00919058', 'NGN': '0.00276871', 'PKR': '0.00863255', 'PEN': '0.306430',
    'PHP': '0.0189146', 'RWF': '0.00114594', 'Somaliland Shilling': '0.00173098',
    'SOS': '0.00173098', 'LKR': '0.00628942', 'SZL': '0.0757967', 'SYP': '0.00194166',
    'TJS': '0.110491', 'TRY': '0.220761', 'UAH': '0.0382074', 'TZS': '0.000439639',
    'YER': '0.00399717', 'ZMW': '0.0983911', 'NIS': '0.279906', 'EGP': '0.0560096'}

# loop over rice
for row in data.itertuples():
    # check if currency in dictonary
    if row.cur_name in conversionDict:
        # calculate update_price with matching key
        update_price = round((row.mp_price * float(conversionDict[row.cur_name])),2)
        # update the values in the dataframe
        data.at[row.Index, 'mp_price'] = update_price
        data.at[row.Index, 'cur_name'] = 'USD'
data.to_csv(path_or_buf="finalRiceDataset.csv")


# voorbeeld voor AFN currency
# variabelen
# currency = 0.0140037
# currencyName = 'AFN'

# loop per rij
# for row in rice.itertuples():
    # if row.cur_name == currencyName:
        # calculate new value
        # new_price = row.mp_price * currency
        # update values
        # rice.at[row.Index, 'mp_price'] = new_price
        # rice.at[row.Index, 'cur_name'] = 'USD'
