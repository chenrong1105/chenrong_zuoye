'''
后裔，后裔继承了Game的hp和power，并多了护甲属性。
重新定义另外一个defense方法：
final_hp = hp+defense-enemy_power
enemy_final_hp = enemy_hp-power
两个hp进行对比，血量先为零的人输掉比赛
'''


import random

from pythoncs.mxdx_demo.mxdx_hhgame_demo2 import Game


class houyi(Game):
    def __init__(self,my_hp,your_hp):
        self.defense = 10
        super().__init__(my_hp,your_hp)

    def fight(self):
        #self.my_hp = 1000
        self.my_power = random.randint(0,1000)
        #self.your_hp = 1000
        self.your_power = random.randint(0,1000)

        while True:
            my_final_hp = self.my_hp +self.defense- self.your_power
            your_final_hp = self.your_hp - self.my_power
            if my_final_hp <=0:
                print("我输了")
                break
            elif your_final_hp <=0:
                print("你输了")
                break
            else:
                print("游戏继续")
                break



houyi = houyi(1000,2000)
houyi.fight()
