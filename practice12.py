#1
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum
print(fact(5))

#2
num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))

#3
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形的面积是%0.2f' % area)

#4
num =int(input("输入一个数，计算阶乘："))
f=1
if num <0:
    print("SORRY,负数没有阶乘")
if num==0:
    print("0的阶乘是1")
else:
    for i in range(1,num+1):
        f=f*i
print("%s的阶乘是%s"%(num,f))

#5
dec = int(input("输入数字："))
print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))
