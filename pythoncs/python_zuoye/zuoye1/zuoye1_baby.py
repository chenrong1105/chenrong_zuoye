'''
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
'''


class Peson:
    def __init__(self, age, weigt, gender):
        self.age = age
        self.weigt = weigt
        self.gender = gender

    def Eat(self):
        print("人会吃饭")

    def run(self):
        print("喜欢跑步")

class Baby(Peson):
    def __init__(self,addr):
        self.addr = addr
        super().__init__(1,3.6,"male")

    def sleep(self):
        print("喜欢睡觉")


# huawei = Peson(60 * 80, "red", "huawei")
# print(huawei.logo)
# A = huawei.Call()

yuanbao = Baby("深圳")
yuanbao.sleep()
print(yuanbao.weigt)
yuanbao.run()