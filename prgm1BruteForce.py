import string
import numpy, matplotlib.pyplot as plt
from itertools import permutations
from math import sqrt
import random

NUMBERS_OF_CITIES = 4
MIN_VALUE_OF_TERRITORY = 0
MAX_VALUE_OF_TERRITORY = 10

def random_generator(size=6, chars=string.ascii_uppercase): #+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def main(): 
    #Variables
    global NUMBERS_OF_CITIES
    global MIN_VALUE_OF_TERRITORY
    global MAX_VALUE_OF_TERRITORY
    citiesList = Cities()
    print(citiesList)
    permsList = []
    permsList.extend(permutations(citiesList))
    statesList = []
    for p in permsList:
        var = Variation()
        p = Cities(p)
        full_distance = 0
        for i in range (NUMBERS_OF_CITIES - 1):
            full_distance += p.distance(i,i+1)
        var.set(p,full_distance)
        statesList.append(var)
    print("All possibilities: ")
    print(statesList)
    statesList = sorted(statesList, key=lambda x : x.fulldistance)
    print("Best variant: ")
    print(statesList[0])

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

if __name__ == '__main__': 
    main()
