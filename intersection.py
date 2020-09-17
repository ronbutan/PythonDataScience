def pair_intersect(a, b):
    n = len(a)
    lstpairs = [[(a[i],b[i]),(a[j],b[j])] for i in range(n-1) for j in range(i+1,n)]
    print(lstpairs)
    i = 0
    for pair in lstpairs:
        p1,p2 = pair
        if (p1[0] > p2[0]) and (p1[1] < p2[1]):
            i += 1
        elif (p1[0] < p2[0]) and (p1[1] > p2[1]):
            i += 1
    return i


a = [1, 2, 3]
b = [2, 1, 3]
print(pair_intersect(a, b))
a = [3,1,-1,0]
b = [0,2,2,3]
print(pair_intersect(a, b))
a = [0,1, 2, 3,4]
b = [0,1, 2, 3,4]
print(pair_intersect(a, b))
a = [-1,0]
b = [0,0]
print(pair_intersect(a, b))
a = [-1,0,1,2,3,4]
b = [4,0,1,2,3,4]
print(pair_intersect(a, b))
a = [-1,0,0,2,2,4]
b = [0,-1,2,1,4,3]
print(pair_intersect(a, b))