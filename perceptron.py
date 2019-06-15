import numpy as np
import string
import matplotlib.pyplot as plt
from itertools import permutations
from math import sqrt
import random

class Percpeptron():
    def __init__(self, data, targets):
        self.data = data
        self.targets = targets
        self.result = [0 for x in range(10)]
        self.b = random.randint(0,1)
        print(self.b)
        self.wA = random.randint(0,1)
        print(self.wA)
        self.wB = random.randint(0,1)
        print(self.wB)
        self.e = 0
           
    def predict(self, inputs):
        summation = 1
        if summation > 0:
          activation = 1
        else:
          activation = 0            
        return activation

    def train(self, next_data):
        self.data = next_data
        w = 10
        h = 2
        for x in range(w):
            a = self.wA * self.data[x][0] + self.wB * self.data[x][1] + self.b
            if a > 1:
                self.result[x] = 1
            else:
                self.result[x] = 0
            self.e = self.targets[x] - a
            if self.e != 0:
                self.wA = self.wA + self.e * self.data[x][0]
                self.wB = self.wB + self.e * self.data[x][1]
                self.b = self.b + self.e

def initData():
    w = 10
    h = 2
    data = [[0 for x in range(h)] for y in range(w)] 
    for x in range(w):
        for y in range(h):
            data[x][y] = random.randint(-20,20)
    return data

def fun(x):
    return x

def initTargets(data):
    w = 10
    h = 2
    targets = [0 for x in range(w)]
    for x in range(w):
        targets[x] = fun(data[x][0])
        # if data[x][1] >= fun(data[x][0]):
        #     targets[x] = 1
        # else:
        #     targets[x] = 0
    return targets

def main(): 
    data = initData()
    print("Dane treningowe: ")
    print(data)
    targets = initTargets(data)
    perc = Percpeptron(data, targets)
    for x in range(10):
        perc.train(data)
        data = initData()
        print("Dane treningowe: ")
        print(data)
        print("Wektor wynikowy: ")
        print(perc.result)
        print("Wartosci wag: ")
        print(perc.wA)
        print(perc.wB)

if __name__ == '__main__': 
    main()