import math
import time
from numpy.random import seed
from numpy.random import randint
import numpy as nup

def functionOfAdaptation(x):
    return 2*(pow(x,2)+1)

#Global variables for changes conditions in algorithm
POPULATION_SIZE = 8 #Selected members of the population

def main(): 
    #Variables
    global POPULATION_SIZE 
    #seed(9001)
    population = nup.empty([POPULATION_SIZE]).astype(int)
    p_values = nup.empty([POPULATION_SIZE]).astype(int)
    p_bin_values = nup.empty([POPULATION_SIZE]).astype(Chromosome)
    next_generation = nup.empty([POPULATION_SIZE]).astype(Chromosome)
    for i in range (POPULATION_SIZE):
        population[i] = nup.random.randint(1,127)
    for i in range (POPULATION_SIZE):
        p_values[i] = functionOfAdaptation(population[i])
    print(population) 
    print(p_values)
    for i in range (POPULATION_SIZE):
        p_bin_values[i] = Chromosome(population[i])
    print(p_bin_values)
    for i in range (POPULATION_SIZE):
        los1 = randint(0,POPULATION_SIZE-1)
        w = 0
        while w==0 :
            los2 = randint(0,POPULATION_SIZE-1)
            if los1!=los2:
                w = 1
        next_generation[i] = p_bin_values[los1].crossingGenes(p_bin_values[los2])
    print(next_generation)

class Chromosome():
    def __init__(self, base):  
        self.base = base
        self.chromosome = self.makeChromosome(base) 

    def makeChromosome(self, base):
        return '{0:08b}'.format(base)

    def __repr__(self):
        return self.chromosome

    def crossingGenes(self, second_chromosome):
        locus = randint(1,6)
        child = self.chromosome[:locus+1]
        child += second_chromosome.chromosome[locus+1:]
        #child = Chromosome(child)
        return child

class Roulette():
    def __init__(self, p_values):
        self.rsum = nup.sum(p_values)
        for i in range (POPULATION_SIZE):
            self.roulette_values = (self.rsum/p_values[i])*100

    def spin(self):   
        result = nup.empty([POPULATION_SIZE]).astype(int)
        for i in range (POPULATION_SIZE):
            lucy = randint(0,self.roulette_values[POPULATION_SIZE-1])
            for j in range (POPULATION_SIZE):
                if lucy <= self.roulette_values[j]:
                    result[i] = self.roulette_values[j]
        return result

if __name__ == '__main__': 
    main() 
