'''异常捕获及处理'''
try:#将被测代码放入try代码块
    num1 = int(input("请输入一个除数："))
    num2 = int(input("请输入一个被除数："))
    print(num1/num2)
# except ZeroDivisionError:#若知道异常名称的话则可提前定义异常名称
#     print("被除数不能为0")
# except ValueError: #若知道异常名称的话则可提前定义异常名称
#     print("输入值类型错误")
except: #若不知道异常名称的话也可以不用定义异常名称
     print("这是一个通用型异常")
else: #若程序没有发生异常则走else语句块并正常运算
    print("程序没有发生异常")
finally: # 不管是否发生异常都会执行的代码块
    print("不管是否发生异常都会执行的代码块")



'''手动抛出异常'''
x = 10
if x>5:
    raise Exception("这是一个异常") #raise Exception手动抛出一个异常



'''自定义异常'''
class MyException(Exception): #自定义异常类需要继承Exception基类
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value1 = value2
raise MyException("value1","value2") #手动抛出一个自定义异常