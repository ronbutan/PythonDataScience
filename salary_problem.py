'''
Categorize employees into 4 salaried bracket
salary based on dollar quantum for lowest salaried worker (<=2000)
remaining based on percentage

'''

salary = [1500, 1500, 1600, 1700, 1750, 1800, 1820, 1850, 1860, 1880, 1900, 2000, 2200, 4500, 6000, 7000, 10000]
# Your code here
num_employees = len(salary)
salary_sorted = sorted(salary)
median = 0
bonus = 2000

# median
if num_employees % 2 == 0: 
    median1 = salary_sorted[num_employees//2] 
    median2 = salary_sorted[num_employees//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = salary_sorted[num_employees//2]

# mean
mean = sum(salary_sorted) / num_employees

maximum = salary_sorted[-1]
minimum = salary_sorted[0]

print('# of employees:', num_employees)
print('sorted', salary_sorted)
print("Median is: " + str(median)) 
print("Mean is : {0:.2f}".format(mean))
print("Max is: " + str(maximum)) 
print("Min is: " + str(minimum)) 

'''
Method #1 - Bonus based solely on salary
'''

lowest = [w for w in salary_sorted if w <= 2000]
low = [w for w in salary_sorted if w > 2000 and w <= 4500]
medium = [w for w in salary_sorted if w > 4500 and w <= 7000]
high = [w for w in salary_sorted if w > 7000]

print('Lowest: {0}, Low: {1}, Medium: {2}, High: {3}'.format(len(lowest),len(low),len(medium),len(high)))


lowestquantum = 80
lowest_bonus = lowestquantum * len(lowest)
lowest = [x + lowestquantum for x in lowest]
left = bonus - lowest_bonus
print('Left: ${0}'.format(left))
lowpercent = 0.4
mediumpercent = 0.35
highpercent = 1 - lowpercent - mediumpercent
lowquantum = (left * lowpercent) / len(low)
print('Low quantum: ${0}, Total: ${1}'.format(lowquantum, lowquantum * len(low)))
low = [x + lowquantum for x in low]
mediumquantum = (left * mediumpercent) / len(medium)
print('Medium quantum: ${0}, Total: ${1}'.format(mediumquantum, mediumquantum * len(medium)))
medium = [x + mediumquantum for x in medium]
highquantum = (left * highpercent) / len(high)
print('High quantum: ${0}, Total: ${1}'.format(highquantum, highquantum * len(high)))
high = [x + highquantum for x in high]

print(lowest,low,medium,high)

lowest.extend(low)
lowest.extend(medium)
lowest.extend(high)
print('New List', lowest)


if num_employees % 2 == 0: 
    median1 = lowest[num_employees//2] 
    median2 = lowest[num_employees//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = lowest[num_employees//2]
mean = sum(lowest) / num_employees

maximum = lowest[-1]
minimum = lowest[0]
print("Median is: " + str(median)) 
print("Mean is : {0:.2f}".format(mean))
print("Max is: " + str(maximum)) 
print("Min is: " + str(minimum)) 