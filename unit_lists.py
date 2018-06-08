import math

###
# a massive function that checks the given measurement trough if-elif statements
# and converts the weight accordingly
##
def convert_weights(weight, measurement)
    if measurement === 'KG':
        new_weight = weight
    elif measurement == 'Pound':
        new_weight = weight*0.45359237
    elif measurement == '90 KG':
        new_weight = weight*90
    elif measurement == 'MT':
        new_weight = weight*1000000000
    elif measurement == '45 KG':
        new_weight = weight*45
    elif measurement == '500 KG':
        new_weight = weight*500
    elif measurement == 'Marmite':
        new_weight = weight*2.72155422
    elif measurement == '100 KG':
        new_weight = weight*100
    elif measurement == '25 KG':
        new_weight = weight*25
    #elif measurement == 'Unit':
    #    new_weight = weight*Onbekend
    elif measurement == '500 G':
        new_weight = weight*0.5
    elif measurement == '400 G':
        new_weight = weight*0.4
    elif measurement == '150 G':
        new_weight = weight*0.15
    # elif measurement == 'Loaf':
    #     new_weight = weight*Onbekend
elif measurement == '1.5 KG':
        new_weight = weight*1.5
    elif measurement == '12.5 KG':
        new_weight = weight*12.5
    elif measurement == '50 KG':
        new_weight = weight*50
    elif measurement == 'Pound':
        new_weight = weight*0.45359237
    elif measurement == '750 KG':
        new_weight = weight*750
    elif measurement == 'Cuartilla':
        new_weight = weight*2.875575
    elif measurement == '125 G':
        new_weight = weight*0.125
    elif measurement == '11.5 KG':
        new_weight = weight*11.5
    elif measurement == '380 G':
        new_weight = weight*0.380
    elif measurement == '385 G':
        new_weight = weight*0.385
    elif measurement == '185 G':
        new_weight = weight*0.185
    elif measurement == '85 G':
        new_weight = weight*0.085
    elif measurement == '91 KG':
        new_weight = weight*91
    elif measurement == '650 G':
        new_weight = weight*0.650
    elif measurement == '115 G':
        new_weight = weight*0.115
    elif measurement == '350 G':
        new_weight = weight*0.350
    elif measurement == '1.8 KG':
        new_weight = weight*1.8
    elif measurement == '2 KG':
        new_weight = weight*2
    elif measurement == '300 G':
        new_weight = weight*0.300
    elif measurement == '160 G':
        new_weight = weight*0.160
    elif measurement == '5 KG':
        new_weight = weight*5
    elif measurement == '200 G':
        new_weight = weight*0.2
    elif measurement == '10 KG':
        new_weight = weight*10
    elif measurement == '750 G':
        new_weight = weight*0.75
    elif measurement == '12 KG':
        new_weight = weight*12
    elif measurement == '18 KG':
        new_weight = weight*18
    elif measurement == '60 KG':
        new_weight = weight*60
    elif measurement == '3 KG':
        new_weight = weight*3
    elif measurement == '3.5 KG':
        new_weight = weight*3.5
    return(round(new_weight, 2))
