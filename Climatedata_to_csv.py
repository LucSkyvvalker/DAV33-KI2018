# Code for converting text data to csv, used for climate data

i = 0
# open the files to read and write
with open("EasternAfrica.txt") as fIn, open("EasternAfrica.csv", "w") as fOut:
    # read lines
    lines = fIn.readlines()
    # loop over lines
    for line in lines:
        # replace spaces with comma's and write the line
        line.replace(" ", ",")
        fOut.write(line)
        i += 1
