''' 两层分支结构：if else'''
a = 1
if a==0:
    print("a=0")
else:
    print("a != 0")

''' 多层分支结构：if elif else'''
b = 1
if b==0:
    print("b=0")
elif b==1:
    print("b=1")
else:
    print("b != 0和1")

''' 实现以下分段函数
     x+3 (x>1)
y=   x+2 (-1<=x<=1)
     5*x+3 (x<-1)
'''
#方案一，嵌套分支结构：
# x =0
# if x>1:
#     y=x+3
# else:
#     if x<-1:
#         y=5*x+3
#     else:
#         y=x+2
# print(f"y={y}")

#方案二,多层分支结构更加推荐的方式：
x =-10
if x>1:
    y=x+3
elif -1<=x<=1:
    y=x + 2
elif x<-1:
    y=5*x+3
print(f"y={y}")


'''循环结构'''

# 1.计算1~100求和
sum1=0
for i in range(0,101):
    sum1=sum1+i
print(f"sum1={sum1}")

#使用python实现0~100之间的偶数就和
#range(开始,截至,步长)
sum2=0
for i in range(0,101,2):
    sum2=sum2+i
print(f"sum2={sum2}")

#加入分支结构实现1~100之间的偶数求和
sum3=0
for i in range(0,101):
    if i%2==0:
        sum3=sum3+i
print(f"sum3={sum3}")

#while循环
while a==1:
    print("a=1")
    a += 1
else:
    print("a!=1")
    print(f"a={a}")

#break和continue区别
for i in range(0,10):
    if i==5:
        break
    print(f"i={i}")


for j in range(0,10):
    if j==5:
        continue
    print(f"j={j}")
"""
猜数字游戏
计算机出一个0~100的随机数字由人来猜
计算机根据人猜出来的数字来判断大一点/小一点/相等
"""
import random
while True:
    your_number = int(input("请输入你的数字："))
    computer_number = random.randint(0, 100)
    print(computer_number)
    if your_number == computer_number:
        print("我们一样大")
        break
    elif your_number > computer_number:
        print("你大我小")
    else:
        print("你小我大")
