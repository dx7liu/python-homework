#1
alist = [73, 66, 57, 10, 2]
blist = alist.copy()
blist.sort()
print(blist)
blist = sorted(alist)
print(blist)
alist = list(range(1, 7))
alist.extend(range(7, 20))
print(alist)
print(blist)
blist.index(2)
print(blist.index(2))
blist.insert(2, 7)
print(blist.index(7))
print(blist)
blist.pop()
print(blist.pop())

#2
atuple = (3, 4, 5)
print(atuple)
print(atuple[2])

#3
x = 3
y = 7
x, y = y, x
print(x, y)

#4
str = "hello, world."
print(str[5])
print(len(str))
print(max(str))
print(str.upper())

str = "Hello, world!"
print(str.lower())
print(2 * str)

#5
for i in range(1, 10):
    print((10 - i) * ' ', (2 * i - 1) * '*')
