'''
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
'''

class Telephone:
    def __init__(self,size,color,logo):
        self.size = size
        self.color = color
        self.logo = logo

    def Call(self):
        print("手机可以打电话")

    def sing(self):
        print("手机可以用来播放音乐")

huawei = Telephone(60*80,"red","huawei")
print(huawei.logo)
A =huawei.Call()