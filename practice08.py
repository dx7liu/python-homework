#1
print('Hello', end='\n')
print('world')

#2
x = 1
y = 2
z = 3
print(x, y, z)
x, y, z = 1, 2, 3
print(x, y, z)
value = 1, 2, 3
print(value)
print(type(value))
x, y, z = value
print(x)
print(y)
print(z)
print(type(x))

#3
x, y, *z = 1, 2, 3, 4
print(x)
print(y)
print(z)
x, *y, z = 1, 2, 3, 4, 5, 6
print(x)
print(y)
print(z)
x, *y, z = 1, 2, 3
print(x)
print(y)
print(z)

#4
name_list = ['liu3', 'wang4', 'li', 'a4']
phone_number_list = [110, 120, 119, 114]
print(name_list)
print(phone_number_list)
index = name_list.index('a4')
print(index)
print(phone_number_list[index])
print(phone_number_list[name_list.index('a4')])

#5
phone_book = {'liu3': 110, 'wang4': 120, 'li': 119, 'a4': 114}
print(phone_book)
print(name_list)
print(type(name_list))
print(type(phone_book))

