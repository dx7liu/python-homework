#1
phone_book = {}
print(phone_book)
phone_book['a3'] = 110
print(phone_book)
phone_book['Li'] = 120
print(phone_book)
phone_book['Wang'] = 119
phone_book['Zha'] = 114
print(phone_book)

#2
name_list = ['Zha', 'Li', 'Wa5', 'Zhao6']
phone_number_list = [110, 120, 119, 114]
for index in range(4):
    print(index)

#3
phone_book1 = {'Zha': 110, 'Li': 120}
phone_book2 = {'Wa5': 119, 'Zhao6': 114}
print(phone_book1)
print(phone_book2)
phone_book1.update(phone_book2)
print(phone_book1)
print(phone_book2)

#4
phone_book = {'Zhang3': 110, 'Li4': 120, 'Wang5': 119, 'Zhao6': 114}
print(phone_book)
phone_book.pop('Zhang3')
print(phone_book)
del phone_book['Li4']
print(phone_book)
print(phone_book.pop('Wang5'))
print(phone_book)

#5
from collections import OrderedDict
ordered_phone_book = OrderedDict()
ordered_phone_book['Zhang3'] = 110
ordered_phone_book['Li4'] = 120
ordered_phone_book['Wang5'] = 119
ordered_phone_book['Zhao6'] = 114
print(ordered_phone_book)
print(type(ordered_phone_book))
print(type(phone_book))