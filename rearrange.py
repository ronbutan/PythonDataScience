def rearrange(l):
    i = 0
    while i < len(l):
        if type(l[i]) in (tuple,list):
            for n in l[i]:
                l.append(n)
            del l[i]
            continue
        elif type(l[i]) == str and len(l[i]) > 1:
            for n in l[i]:
                l.append(n)
            del l[i]
            continue
        else:
            i += 1
    print(l)

rearrange([1, 2.0, [None,[3,True]], 'ab', [100, 200], ('o', 12)])
rearrange([[1, ''], ('w', 'xy'), 'abc', 4.5, 2])


# l = [1,2,3,[10,20,['c','d',90]],['a','b'],4,5,'z']
# i = 0
# while i < len(l):
#     print(i)
#     if type(l[i]) in (tuple,list):
#         for n in l[i]:
#             l.append(n)
#         del l[i]
#         continue
#     elif type(l[i]) == str and len(l[i]) > 1:
#         for n in l[i]:
#             l.append(n)
#         del l[i]
#         continue
#     else:
#         i += 1
# print(l)

# for i in (1,2,3):
#     print(i)
#P = 1
#print(type(P) in (tuple, list, str))