"""函数的定义
1.位置参数传参需一一对应
2.return可以返回任何东东，只写return或者不写return返回值是个none
"""
def func1(a,b,c):
    '''
    此处三个引号后会自动生成这段给程序员看的注释：
    函数func1的作用
    :param a: a参是干哈的
    :param b: b参是干哈的
    :param c: c参是干哈的
    :return: 函数最终返回个啥
    '''
    print("这是一个函数")
    print("这是一个参数a",a)
    #pycharm快捷键ctrl+d 快速复制一行
    print("这是一个参数b",b)
    print("这是一个参数c",c)
    return "444"
'''函数的调用'''
print(func1(1, 2, 3))

'''传参
1.默认参数:调用时不传即取默认设置值，传了参数话就会用传递参数的值
2.关键字参数：k=v的形式传递，关键字参数必须跟随在位置参数的后面
3.Lambda表达式
'''
def func2(a1=2):
    print("参数a的值为：",a1)

func2()



def func3(a2,b=3):
    print("参数a的值为：",a2)
    print("参数b的值为：", b)

func3(31)

func4 =  lambda x: x*3
print(func4(2))

def func5(x):
    return x*3
print(func5(2))

func6 = lambda x,y:x+y
print(func6(3,9))

