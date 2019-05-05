import string
import numpy, matplotlib.pyplot as plt
from itertools import permutations
from math import sqrt
import random

NUMBERS_OF_CITIES = 4
MIN_VALUE_OF_TERRITORY = 0
MAX_VALUE_OF_TERRITORY = 10
START_CITY = 0

def random_generator(size=6, chars=string.ascii_uppercase): #+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def main(): 
    #Variables
    global NUMBERS_OF_CITIES
    global MIN_VALUE_OF_TERRITORY
    global MAX_VALUE_OF_TERRITORY
    global START_CITY
    citiesList = Cities()
    print(citiesList)
    statesList = []
    statesList.append(citiesList.cities[START_CITY])
    now_in = 0
    best_option = citiesList.cities[START_CITY]
    best_distance = distance(statesList[now_in],citiesList.cities[START_CITY+1])*2
    full_distance = 0
    for i in range(len(citiesList.cities)-1):
        best_distance = best_distance*2
        for c in citiesList:
            if not c in statesList:
                d = distance(statesList[now_in],c)
                if d < best_distance:
                    best_option = c
                    best_distance = d
                    full_distance += best_distance
        now_in += 1
        statesList.append(best_option)
    print(statesList)
    print(full_distance)

class City:
    def __init__(self, name):  
        self.name = name
        self.x = random.randint(MIN_VALUE_OF_TERRITORY,MAX_VALUE_OF_TERRITORY)
        self.y = random.randint(MIN_VALUE_OF_TERRITORY,MAX_VALUE_OF_TERRITORY)

    def __repr__(self):
        return str(self.name) + " < " + str(self.x) + ", " + str(self.y) + " >"

class Cities:
    def __init__(self, cities = []):  
        self.cities = []
        if len(cities) == 0:
            for i in range (NUMBERS_OF_CITIES):
                name = random_generator(3)
                cities.append(City(name))
        self.cities.extend(cities)

    def __repr__(self):
        result = ""
        for m in range (NUMBERS_OF_CITIES):
            result = result + "\nCity number: " + str(m) + " " + str(self.cities[m])
        return result

    def __iter__(self):
        return iter(self.cities)

    def distance(self, nrA, nrB):
        d = sqrt((self.cities[nrA].x - self.cities[nrB].x)**2 + (self.cities[nrA].y - self.cities[nrB].y)**2)
        return d

class Variation:
    def __init__(self):  
        self.sequence = [NUMBERS_OF_CITIES]
        self.fulldistance = 0

    def set (self, sequence, fulldistance):
        self.sequence = sequence
        self.fulldistance = fulldistance

    def __repr__(self):
        return str(self.sequence) + "\ndistance=" + str(self.fulldistance)

def distance(A, B):
    d = sqrt((A.x - B.x)**2 + (A.y - B.y)**2)
    return d

if __name__ == '__main__': 
    main()
