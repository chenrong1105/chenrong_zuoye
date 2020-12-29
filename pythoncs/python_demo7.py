import json
'''字面量插值'''
#一、格式化输出,需要知道变量的具体类型
name = "chenrong"
age = 28
print("my name is %s,my age is %d,num is %.2f"%(name,age,3.1514926))
#二、format输出,不需要知道变量的具体类型,同一变量可以被多次引用
print("my name is {0},my age is {1},num1 is {2},num2 is {2}]".format(name,age,3.1514926))
print("my name is {},my age is {},num1 is {}".format(name,age,3.1514926))

list1=[1,5,3]
dict1={"name":"chenrong","gender":"female"}
print("my list is {},my dict is {}".format(list1,dict1))

namelist = ["zhangsan","lisi","wangwu"]
print("our term are {}、{} and {}".format(*namelist)) #列表解包

print("my name is {name},my gender is {gender}".format(**dict1)) #字典解包

#二、f'{变量名}' 格式输出，python3.6以上版本才支持，大括号里可以是表达式或函数;大括号内不能转义，不能使用"\",大括号外可以使用
print(f"my name is {name},my age is {age},my list is \n{list1[1]},my dict is {dict1['name']}")
print(f"my name is {name.upper()}") #大括号里可以支持函数
print(f"result is {(lambda x:x+1)(2)}") #大括号里可以支持表达式，如果大括号内出现：，则用（）将表达式包裹起来

'''文件的读取步骤：打开、操作、关闭'''
# f = open("b/test1.txt") #打开文件
# # print(f.readlines()) #读取文件内的所有内容
# print(f.readline()) #按行读取文件的内容
# f.close()#关闭文件，释放资源

#with语句块，可以将文件打开之后操作完毕自动关闭文件
#图片的读取需要使用rb二进制格式读取，正常的文本可以使用rt格式（默认格式）读取
with open("b/test1.txt") as f:
    print(f.readlines())

'''json格式转化'''
#json是由列表或字典组成
date = {
    "name":["chenrong","xiaochen"],
    "age":26,
    "gender":"female"
}
print(type(date))
date1 = json.dumps(date)#json.dumps将json格式转化为str类型
print(date1)
print(type(date1))

date2 = json.loads(date1)#json.loads将str格式转化为json类型
print(date2)
print(type(date2))