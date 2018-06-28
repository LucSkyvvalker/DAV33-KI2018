import pandas as pd

###
# this is an example, this loop also runs for the other common commodities
###


# loop over the dataset and write all matches to knew file
counter = 0
with open('dataset.csv', encoding="latin-1") as fIn, open("Riceset.csv", "w", encoding="latin-1") as fOut:
    for line in fIn:
        if 'Rice' in line:
            fOut.write(line)
            counter += 1
        # dont forget the column names
        elif counter == 0:
            fOut.write(line)
            counter += 1
