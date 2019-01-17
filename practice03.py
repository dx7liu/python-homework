#1
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7];
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

#2
var1 = 'Hello World!'
var2 = "Runoob"
print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

#3
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

#4
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8;
dict['School'] = "菜鸟教程"
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

#5
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))