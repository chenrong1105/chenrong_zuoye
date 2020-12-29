import os
import time
import urllib.request
import math

'''os库常见用法'''
#os.mkdir("testdir") #创建目录
# # os.removedirs("testdir") #删除目录
# print(os.getcwd()) #获取当前目录
# print(os.listdir("./")) #获取当前路径下的文件及文件目录

#在指定目录创建文件并写入文件的内容
# print(os.path.exists("b"))
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt","w")
#     f.write("hello,xiaohuozi")
#     f.close()

'''time库常见用法'''
# print(time.asctime())
# print(time.time()) #时间戳，独一无二
# print(time.localtime()) #返回的是一个元祖
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #time.strftime(格式，元祖)
# print(time.strftime("%Y:%m:%d %H:%M:%S", time.localtime())) #time.strftime(格式，元祖)
# print(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime())) #time.strftime(格式，元祖)

#获取两天前的当前时间
# now_timestamp = time.time()#获取当前时间
# two_timestamp = now_timestamp-60*60*24*2 #计算出两天前当前时间的时间戳
# tuple_time = time.localtime(two_timestamp) #两天前当前时间的时间戳转换为元祖格式
# print(time.strftime("%Y-%m-%d %H:%M:%S", tuple_time)) #将元祖格式转换为期望格式显示出来

# '''urllib库常见用法'''
# respose = urllib.request.urlopen("https://www.baidu.com/")
# print(respose.status)

'''math库常见用法'''
print(math.ceil(5.4))#返回大于等于5.4的最小整数，上限
print(math.floor(5.5))#返回小于等于5.5的最小整数，下限
print(math.sqrt(16)) #返回某个值的开方根
