# ctrl+鼠标点击跳转到对应函数的代码说明页面
'''列表'''
#列表的定义及可变性（支持增删改查）
list1= [4,8,2,6,88,7]
list1[0]=41
print(list1)
list1.append(1234)
print(list1)
list1.insert(0,9)
print(list1)
list1.copy()
print(list1)
list1.remove(6)
print(list1)
list1.sort()#升序排列
print(list1)
list1.sort(reverse=True) #降序排列
print(list1)
list1.reverse() #将数据反向展示
print(list1)
list1.pop(3) #删除指定位置的数据
print(list1)
print(list1.count(8))

# '''生成一个平方列表，如[1,4,9...]，用两种方式实现'''
# #方式一，for循环
list2=[]
for x in range(11):
    list2.append(x**2)
print(list2)
#
list21=[]
for x in range(11):
    if x%2==0:
        list21.append(x**2)
print(list21)

#嵌套循环：满足外层条件下，先里后外执行
list210=[]
for x in range(1,4):
    for y in range(1,4):
        list210.append(x*y)
        print("x*y=",list210)

# #方式二，列表推导式
list3=[x**2 for x in range(11)]
print(list3)

list31=[x**2 for x in range(11) if x%2==0]
print(list31)

list310=[x*y for x in range(1,4) for y in range(1,4)]
print(list310)
'''元祖'''
# #元祖的定义
tuple1=(1,5,6,5,6)
tuple2=4,5,6
print(type(tuple1))
print(type(tuple2))
# #元祖不可变,不支持增删改
print(tuple1.count(5)) #查找5在tuple1出现的次数
print(tuple1.index(6)) #查找6在tuple1首次出现的位置
#
# '''集合'''
# #集合的定义
a = {2} #定义一个非空集合
b = set() #定义一个空集合只可以这样定义，不可用b={}定义空集合
print(type(a))
print(len(b))
print(type(b))
a1={1,5,6}
b1={5,8,6}
print(a1.union(b1)) #求a1和b1的并集
print(a1.intersection(b1)) #求a1和b1的交集
print(a1.difference(b1)) #求a1和b1的差集,a1有但是b1没有的值
a1.add(9) #a1添加新元素
print(a1)
# #集合的列表推导式
print({i for i in "aawefwfadwf"}) #求集合存在的不重复元素

'''字典'''
#字典的定义及常用函数，key值不可变
a1 = {"a":1,"b":2}
b1 = dict(a=1,b=2)
print(type(b1))
print(a1.keys())#获取a1的key值
print(a1.values()) #获取a1的value值
print(a1.items()) #获取a1的键值对值
a1.pop("a") #根据key值删除其对应的键值对
print(a1)
a={}
b=a.fromkeys((1,2,3),"w")#将1,2,3分别设置为a的key值
print(b)
