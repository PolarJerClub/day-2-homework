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

new_list = [i.strip().title() for i in names_list]
a_list = [i for i in new_list for x in i if x=='A']

print(a_list)

#Question 5
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
