from random import randint
from math import sqrt
import numpy, matplotlib.pyplot as plt
#miasta = {"Nr": 0, "Ox": 0, "Oy": 0}
miasta = {}
way_to_now = {}

for m in range (4):
    # miasta["Nr"] = m
    # miasta["Ox"] = randint(0,10)
    # miasta["Oy"] = randint(0,10)
    miasta[m] = [randint(0,10), randint(0,10)]

for m in range (4):
    print("Miasto numer: ", m, miasta[m])

#długość drogi miedzy miastami
def distance(miasta, nrA, nrB):
    if miasta[nrA][0] is None and miasta[nrB][0] is None and miasta[nrA][1] is None and miasta[nrB][1] is None:
        d = sqrt((miasta[nrA][0]-miasta[nrB][0])**2 + (miasta[nrA][1]-miasta[nrB][1])**2)
        return d

def take_best_way(miasta, nr_now, maxi):
    d = {}
    for i in range(1,maxi+1):
        d[i-1] = distance(miasta,nr_now,i)
    city_direction = {}
    city_direction[0]=0
    city_direction[1]=1
    print 
    for m in range(maxi):
        if m==0 :
            city_direction[0] = d[m]
        elif city_direction[0]>d[m]:
            city_direction[0]=d[m]
            city_direction[1] += m 
    return city_direction

nr_now = 0
maxi = 3
for i in range(3):
    way_to_now[i] = take_best_way(miasta,nr_now,maxi)
    nr_now = way_to_now[i][1]
    del miasta[way_to_now[i][1]]
    maxi -= 1

print(way_to_now)
plt.plot([miasta[i] for i in range(16)],[miasta[i] for i in range(16)])
plt.plot(way_to_now,way_to_now)
plt.show()