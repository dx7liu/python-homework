#1
def hcf(x, y):
    """该函数返回两个数的最大公约数"""
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))

#2
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
print(num1, "和", num2, "的最小公倍数为", lcm(num1, num2))

#3
import calendar
monthRange = calendar.monthrange(2016,9)
print(monthRange)

#4
import datetime
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday
print(getYesterday())

#5
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2;
print(tup3)