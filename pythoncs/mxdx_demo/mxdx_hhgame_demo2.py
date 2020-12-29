'''
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''


import random
class Game:
    def fight(self):
        self.my_hp = 3
        self.my_power = random.randint(0,3)
        self.your_hp = 3
        self.your_power = random.randint(0,3)
        while True:
            my_hp = self.my_hp - self.your_power
            your_hp = self.your_hp - self.my_power
            if my_hp <=0:
                print("我输了")
                break
            elif your_hp <=0:
                print("你输了")
                break
            # else:
            #     print("平局")



A = Game()
A.fight()
