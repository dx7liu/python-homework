#1
import numpy
variable = numpy.array([1, 2, 3, 4, 5])
print(variable)
print(numpy.max(variable))
print(numpy.mean(variable))

#2
import numpy as np
variable1 = np.array([3, 4, 5, 6, 7, 8])
print(np.mean(variable1))
from numpy import mean
print(variable1)
print(mean(variable1))

#3
list_variable = ['a', 'b', 'dd', 'cccc']
print('a' in list_variable)
print('aa' in list_variable)

#4
list_1 = []
dict_1 = {}
for index in range(1000000):
    list_1.append(index)
    dict_1[index] = index
list_2 = []
dict_2 = {}
for index in range(10000000):
    list_2.append(index)
    dict_2[index] = index
print(len(list_1))
print(len(dict_1))
print(len(list_2))
print(len(dict_2))

#5
import datetime
search_value = list_1[-1]
start_time = datetime.datetime.now()
print(search_value in list_1)
end_time = datetime.datetime.now()
print(end_time - start_time)

