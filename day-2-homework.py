#Question 1
alist = [1,11,14,5,8,9]
blist = []
for num in alist:
    if num < 10:
        blist.append(num)
    
print(blist)

#Question 2
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
l_3 = l_1 + l_2

print(sorted(l_3))

#Question 3
sq = range(1,16)

for num in sq:
    print(num**2)

#Question 4
names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
#expected output = ['Amy', 'Alex']
names_list2 = names_list.sort()
sorted = []
final = []

for i in names_list:
    sorted += [i.strip('[ ]').title()]
#     print(sorted)
for i in sorted:
    for x in i:
        if x == "A":
            final.append(i)
print(final)

#Question 5
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)