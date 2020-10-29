import numpy as np
import math
from itertools import permutations

def euclidean_dist(e,r):
    diff = e - r
    diff = np.sqrt(np.sum(diff**2))
    return 1 - diff

def compensate(e,r,avg):
    pair = np.asarray(list(zip(e,r)))
    amt = 0
    r = 0
    for e,r in pair:
        euc = euclidean_dist(e,r)
        if euc > avg:
            r = (1 - euc) * ((euc - avg)/avg) + euc
        else:
            r = euc * (1 - avg)
        amt += 1000 * (1 - r)
    return amt

def no_replacement(employee, restaurant, avg):
    lres = np.asarray(list(permutations(restaurant)))
    lamt = []
    for i in lres:
        amt = compensate(employee,i,avg)
        lamt.append(amt)
    print("***No replacement***")
    print("The minimum amount to compensate is ${0:.2f}".format(min(lamt)))
    print("The maximum amount to compensate is ${0:.2f}".format(max(lamt)))

def with_replacement(employee,restaurant,avg):
    euc = np.asarray([[euclidean_dist(e,r) for r in restaurant] for e in employee])
    euc = np.asarray([[(1 - score) * ((score - avg)/avg) + score if score > avg else score * (1-avg) for score in e] for e in euc])
    empXres = np.asarray([[1000 * (1 - score) for score in euc[0]] for e in euc])
    small = np.sum(np.minimum.reduce(empXres,axis=1))
    big = np.sum(np.maximum.reduce(empXres,axis=1))
    print("***With replacement***")
    print("The minimum amount to compensate is ${0:.2f}".format(small))
    print("The maximum amount to compensate is ${0:.2f}".format(big))

employee = [(0.6,0.2,0.2),(0.8,0.1,0.1),(0.75,0.1,0.15),(0.5,0.1,0.4),(0.4,0.4,0.2)]
restaurant = [((80,60,60),(70,60,70),(70,60,75)),((70,60,70),(65,70,70),(60,65,80)),((90,80,90),(90,85,95),(90,85,90)),((60,80,70),(55,85,70),(50,80,75)),((75,75,80),(75,75,85),(80,85,80))]
employee = np.asarray(employee)
restaurant = np.asarray(restaurant)

restaurant_mean = np.mean(restaurant,axis=1)
r_mean_norm = [i / sum(i) for i in restaurant_mean]

m = np.asarray([[euclidean_dist(e,r) for r in r_mean_norm] for e in employee])
overall_avg = np.average(m)

no_replacement(employee,r_mean_norm,overall_avg)
with_replacement(employee,r_mean_norm,overall_avg)