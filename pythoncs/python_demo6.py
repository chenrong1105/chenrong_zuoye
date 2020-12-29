'''导入系统自带模块'''
import os
import time
import json



time.sleep(2)
# json.loads()

'''导入第三方模块,需要提前安装,如pip install selenium'''
import yaml
import selenium
import appium

'''导入自定义模块，自定义模块命名不能和系统自带模块或第三方模块重名'''
from pythoncs.python_demo4 import func2
func2(6)

#dir()可以查看当前模块调用了哪些模块
print(dir())
#dir(模块名)可以查看当前模块可以调用指定模块的哪些方法
print(dir(time))