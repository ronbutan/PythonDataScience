def rearrange(l):
    i = 0
    while i < len(l):
        if (type(l[i]) in (tuple,list)) or (type(l[i]) == str and len(l[i]) > 1):
            for n in l[i]:
                l.append(n)
            del l[i]
            continue
        else:
            i += 1
    print(l)

rearrange([1, 2.0, [None,[3,True]], 'ab', [100, 200], ('o', 12)])
rearrange([[1, ''], ('w', 'xy'), 'abc', 4.5, 2])