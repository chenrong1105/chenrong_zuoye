'''
写一个Bicycle(自行车)类，有run（骑行）方法，调用时显示骑行里程km（骑行里程为传入的数字）：
再写一个电动自行车类EBicycle，其继承Bicycle(自行车)类，添加电池电量valume属性通过参数传入，同时有两个方法：
1.fill_charge(vol)用来充电，vol为电量
2. run(km)方法用于骑行，每骑行10km消耗电量1度，当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，
显示骑行结果
'''

#光标放在方法名上，使用Alt+回车快捷键执行导入的动作

class Bicycle:
    def run(self,km):
        print(f"我今天用脚踩了{km}公里")

# chenrong_Bicycle = Bicycle()
# chenrong_Bicycle.run(10)

class EBicycle(Bicycle):
    #如果属性需要传参定义，那么使用构造函数
    def __init__(self,valume):
        self.valume = valume

    def fill_charge(self,vol):
        #现有电量=本身已有电量+充电量
        self.valume = self.valume + vol

        print(f"我充了{vol}度电，现有电量为{self.valume}")

    def run(self,km):
        '''
        run(km)方法用于骑行，每骑行10km消耗电量1度，当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，
        显示骑行结果
        '''
        #1.获得目前电量所能电动骑行的最大里程数
        power_km = self.valume*10
        #如果目前电量所能电动骑行的最大里程数大于要骑行的里程数，那么全程用电瓶就足够了
        if power_km >=km:
            print(f"我今天总共骑行了{km}公里")
        else:
            print(f"我使用电瓶骑行了{power_km}公里")
            #使用非继承调用
            # chenrong_Bicycle = Bicycle()
            # chenrong_Bicycle.run(km - power_km)
            #使用继承调用
            super().run(km - power_km)

xiaoqiang_EBicycle = EBicycle(1.5)
xiaoqiang_EBicycle.fill_charge(1)
xiaoqiang_EBicycle.run(30)
