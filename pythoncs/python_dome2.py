'''
变量命名规范：
1.大小写字母下划线数字组成，不能由数字开头
2.大小写敏感
3.不能和关键字及系统保留字冲突
4.可遵循驼峰命名法
'''

''' 类型一：数字 '''
a=1
print(a)
#id(a)变量a的内存地址
print(id(a))
# 数据类型
int_a = 1
float_a = 0.1
complex_a = 0.2j
# 通过type()查看变量的数据类型
print(type(int_a))
print(type(float_a))
print(type(complex_a))

'''类型二：字符串:

\：转义符
r：忽略转义符作用
+:字符串拼接
切片:[start:stop:step],即[开始:结束-1:步长]
'''
str_a0 = "aass\n" #\n换行
str_a1 = "aass\\n" #\\n 打印出\n
str_a2 = r"aass\n" #r 打印出\n
str_a3 = "bbbbb"
str_a4 = "12345678"
print(str_a0)
print(str_a1)
print(str_a2)
print(str_a2+str_a3)
print(str_a4[0:3])
print(str_a4[0:6:2])
print(str_a4[::-1]) #实现字符串倒序排列

'''
类型三：列表
'''
list = [1,2,3,4,5,6] #定义列表
print(list[0]) #索引
print(list[1:4:2]) #切片
print(list[::-1]) #实现列表倒序排列
