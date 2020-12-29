'''
作业2
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''

class TongLao:
    def __init__(self,my_hp,my_power):
        self.my_hp = my_hp
        self.my_power = my_power

    def see_people(self,name):
        self.name = name

        if self.name == "无崖子":
            print("师弟！！！！")
        elif self.name == "李秋水":
            print("呸，贱人")
        elif self.name == "丁春秋":
            print("叛徒！我杀了你")

    def fight_zms(self,your_hp,your_power):
        self.your_hp = your_hp
        self.your_power = your_power

        self.my_power=self.my_power*10
        self.my_hp=self.my_hp/2

        print(f"我现在的武力值是{self.my_power}")
        print(f"我现在的血量是{self.my_hp}")

        self.my_power = self.my_hp - self.your_power
        self.your_power = self.your_hp -self.my_power

        if self.my_power > self.your_power:
            print("我赢了！")
        else:
            print("你赢了")




