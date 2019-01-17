#1
print('Hello World!')

#2
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')
sum = float(num1) + float(num2)
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))


#3
import random
print(random.randint(0, 9))


#4
num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))

#5
year = int(input("输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print("{0} 不是闰年".format(year))




