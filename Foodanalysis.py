import pandas as pd
data = pd.read_csv("dataset.csv")
import math
import numpy as np
import matplotlib.pyplot as plt


#Print alle landen en zoek naar NaN
countries = []
def printCountries():
    counter = 0
    for country in data.adm_name: #voor 4000 zit er nan bij????
        if country not in countries:
            countries.append(country)
        if country == np.nan:
            counter += 1
    print(countries)
    print(counter)
    print(data.adm_name[400]) 

#Print een overzicht van alle jaren in de database
def printYears():
    print(data.mp_year.describe())
    print(data.mp_year.value_counts())

#List all types of food
def foodTypes():
    foods = []
    for food in data.cm_name:
        if food not in foods:
            foods.append(food)
    print(foods)

#List all different variations of the same commodity
allwheat = []
def allTypesPerFood():
    data.cm_name.value_counts()[:20].plot(kind="bar")
    allrices = []
    for commodity in data.cm_name.unique():
        if "Rice" in commodity:
            allrices.append(commodity)
        
    print(allrices)

    
    for commodity in data.cm_name.unique():
        if "Maize" in commodity:
            allwheat.append(commodity)
    print(allwheat)

def totalFoodPerCountry():
    totalrice = {"fasdf": "asdf"}
    for country in countries:
        totalrice[country] = 0
    for rice in allwheat:
        iscommodity = data.cm_name == rice
        for country in countries:
            iscountry = data.adm_name == country
            totalrice[country] += len(data[iscommodity&iscountry])
        print(rice)
    print(totalrice)
printCountries()
allTypesPerFood()
totalFoodPerCountry()



