import re

p = re.compile('b[a-z]d')
m1 = p.match('bed d bad bd')
m2 = p.match('b bed d bad bd')
m3 = p.search('b bed d bad bd')
m4 = p.findall('b bed d bad bd')
m5 = p.finditer('b bed d bad bd')
print('m1=',m1)
print('m2=',m2)
print('m3=',m3)
print('m4=',m4)
print('m5=',m5)
for s in m5:
    print(s)

print("\\s")