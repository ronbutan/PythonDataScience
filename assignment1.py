

def histogram(ints, sym): # don't change the function definition and the parameter list, otherwise no point will be given.
    result = ''
    if ints is None:
        print()
        return
    largest = max(ints)
    for i in range(largest):
        l = [sym if n > 0 else ' ' for n in ints]
        ints = [n - 1 for n in ints]
        result = ' '.join(l) + '\n' + result
    return result

def histogram2(ints, sym):
    cols = len(ints)
    height = max(ints)
    lstsymbols = [[sym] * n + [' '] * (height - n) for n in ints]
    lstsymbols = [[row[i] for row in lstsymbols] for i in range(cols,-1,-1)]
    return '\n'.join(map(' '.join, lstsymbols))

print(histogram([2, 1, 3, 4, 7, 10, 8, 1, 5, 1], '#'))
print(histogram([4, 1, 3, 5], '$'))
print(histogram2([2, 1, 3, 4, 7, 10, 8, 1, 5], '#'))

# lst = [1, 5, 7, 8, 9, 4, 3] 
 
# res = list(map(lambda x:print('*' * x), lst))
 
# print(res)

# a = [[' ',' ','*',' '],[' ','*','*','*'],['*','*','*','*']]
# print('\n'.join(map(' '.join, a)))



# b = list(x)
# #convert the map into a list, for readability:
# print(list(zip(*b)))

# y = [['*']*10] * 10
# print(['+'] * 2 + (['-'] * 9 if 2 > 3 else []))

M = [['1','2','3'],
    ['4','5','6'],
    ['7','8','9']]

MT = [[row[i] for row in M] for i in range(3)]
print(MT)
print('\n'.join(map(' '.join, MT)))

l = [1,2,3]
print(l[-3])