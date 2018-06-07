import pandas as pd

###
# this is an example, this loop also runs for the other common commodities
###


# loop over the dataset and write all matches to knew file
with open('dataset.csv') as fIn, open("Riceset.csv", "w") as fOut:
    for line in fIn:
        if 'Rice' in line:
            fOut.write(line)
