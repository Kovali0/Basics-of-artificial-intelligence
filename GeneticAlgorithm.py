import math 
import numpy as nup
from random import randint

#Variables
elected_number = 8 #Selected members of the population
S = nup.arange(1,127)
P = nup.empty([elected_number])
P_values = nup.empty([elected_number]).astype(int)
P_bin_values = nup.empty([elected_number]).astype(int)

#Methods
def fun(x):
    return 2*(pow(x,2)+1)

def randomPopulation():
    #P = nup.random.randint(1,127,elected_number)
    for j in range (elected_number):
        P[j] = nup.random.randint(1,127)
    for i in range (elected_number):
        P_values[i]=fun(P[i])
        #P_bin_values[i]=bin(P_values[i])
   
#Main program   
randomPopulation()
print(P)
print(P_values)
print(P_bin_svalues)