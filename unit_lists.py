import math

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
    elif measurement == 'Pound':
        new_weight = weight*0.45359237
    return(round(new_weight, 2))
