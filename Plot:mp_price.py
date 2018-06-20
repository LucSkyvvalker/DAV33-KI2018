# plot all the countries with mp_price
countries = list(rice['adm0_name'].unique())
com = list(rice['cm_name'].unique())
for country in countries:
    land = rice['adm0_name'] == country
    for cm in com:
        c = rice['cm_name'] == cm
        df = rice[land & c]
        if not df.empty:
            fig, ax = plt.subplots()
            x = [df['date']]
            y = [df['mp_price']]
            plt.plot(x, y, 'xb-')
            ax.grid()
#             plt.plot(x, y, 'ro')
            title = country + cm
            plt.title(title)
            plt.show()