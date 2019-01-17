#1
alist = list()
print(alist)
alist = list(range(1, 10))
print(alist)
for number in alist:
    print(number * number)

#2
for x in alist:
    for y in alist:
        if (x <= y):
            print('{}*{}={}'.format(x, y, x * y), end='\t')
        else:
            print('', end='\t')
    print('')

#3
alist = list(range(1, 17))
print(alist)
blist = list(range(17, 23))
print(blist)
print(alist + blist)
print(alist)
alist.append(blist)
print(alist)
alist[9:] = []
print(alist)
for n in blist:
    alist.append(n)
print(alist)
alist[3:3] = (3.5,)
print(alist)
alist[3:4] = []
print(alist)
print(len(alist))
print(min(alist))


#4
t = ['hello', 7, 'test', '7', 3.14]
print(t)

#5
alist = [3, 66, 7, 10, 2]
alist.sort()
print(alist)
alist.reverse()
print(alist)
print(alist.reverse())
print(alist.sort())
blist = alist
blist.sort()
print(blist)