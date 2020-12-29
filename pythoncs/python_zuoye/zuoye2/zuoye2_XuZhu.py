'''
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
'''
from pythoncs.python_zuoye.zuoye2.zuoye2_TongLao import TongLao


class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")

zhangsan = TongLao(15,3)
zhangsan.see_people("李秋水")
zhangsan.fight_zms(15,5)

# lisi = XuZhu(10,2)
# lisi.read()
# lisi.fight_zms(15,6)