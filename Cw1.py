from random import randint
from math import sqrt
#miasta = {"Nr": 0, "Ox": 0, "Oy": 0}
miasta = {}

for m in range (4):
    # miasta["Nr"] = m
    # miasta["Ox"] = randint(0,10)
    # miasta["Oy"] = randint(0,10)
    miasta[m] = [randint(0,10), randint(0,10)]

for m in range (4):
    print("Miasto numer: ", m, miasta[m])

#długość drogi miedzy miastami
def distance(miasta, nrA, nrB):
    d = sqrt((miasta[nrA][0]-miasta[nrB][0])**2 + (miasta[nrA][1]-miasta[nrB][1])**2)
    return d

distance(miasta,0,1)

def take_best_way(miasta):
    d = {}
    for i in range(1,3):
        d[i] = distance(miasta,0,i)
    w=0
    for m in range(3):
        if m==0 :
            w=d[m]
        elif w>d[m]:
            w=d[m]
    print(w)

take_best_way(miasta)