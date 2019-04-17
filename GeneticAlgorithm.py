import math
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
    seed(1)
    population = nup.empty([POPULATION_SIZE]).astype(int)
    p_values = nup.empty([POPULATION_SIZE]).astype(int)
    p_bin_values = nup.empty([POPULATION_SIZE]).astype(Chromosome)
    for i in range (POPULATION_SIZE):
        population[i] = nup.random.randint(1,127)
    for i in range (POPULATION_SIZE):
        p_values[i] = functionOfAdaptation(population[i])
    print(population) 
    print(p_values)
    for i in range (POPULATION_SIZE):
        p_bin_values[i] = Chromosome(population[i])
    print(p_bin_values)

class Chromosome():
    def __init__(self, base):  
        self.base = base
        self.chromosome = self.makeChromosome(base) 

    def makeChromosome(self, base):
        return '{0:08b}'.format(base)

    def __repr__(self):
        return self.chromosome

    #def crossingGenes(self, second_chromosome):


if __name__ == '__main__': 
    main() 
