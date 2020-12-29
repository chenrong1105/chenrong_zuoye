import pytest
import yaml

from pytestsc.zhibo_ketang.be_test.calculate import Calculate
from pytestsc.zhibo_ketang.test_demo.test_getdatas import Testgetdatas

getdatas = Testgetdatas()


# def get_adddatas():
#     with open("datas/calc_add.yml", encoding="utf-8") as f:
#         mydatas = yaml.safe_load(f)
#         adddatas = mydatas['add']['datas']
#         addmyids = mydatas['add']['myids']
#         return [adddatas,addmyids]


#如果这个类下的所有测试用例都需要用到这组测试数据，那么可以将这组测试数据放到类前面（这种情况很少见，毕竟期望值不一样的概率很高）
# @pytest.mark.parametrize('a,b,expect', [
#     (1.5, 0.6, 2.1),
#     (5, 6, 11),
#     (-1, -5, -6)
# ], ids=['浮点数', '正数', '负数'])


class Testcalc:
    def setup_class(self):
        print("开始计算")
        self.cal=Calculate()

    def teardown_class(self):
        print("结束计算")

    # @pytest.mark.parametrize('a,b,expect',[
    #     (1.5,0.6,2.1),
    #     (5,6,11),
    #     (-1,-5,-6)
    # ],ids=['浮点数','正数','负数'])
    @pytest.mark.parametrize('a,b,expect',getdatas.test_get_adddatas()[0],ids=getdatas.test_get_adddatas()[1])
    def test_add(self,a,b,expect):
        result_add = round(self.cal.add(a,b),2)
        assert expect==result_add

    @pytest.mark.parametrize('a,b,expect', [
        (0.1, 0.2, 0.3),
        (0.1, 0.1, 0.2)
    ])
    def test_add_float(self, a, b, expect):
        result_add = round(self.cal.add(a, b),2)  #round()函数四舍五入
        assert expect == result_add

    # @pytest.mark.parametrize('a,b,expect',[
    #     (1.5,0.6,0.9),
    #     (5,6,-1),
    #     (-1,-5,4)
    # ],ids=['浮点数','正数','负数'])
    @pytest.mark.parametrize('a,b,expect',getdatas.test_get_subdatas()[0],ids=getdatas.test_get_subdatas()[1])
    def test_sub(self,a,b,expect):
        result_sub = round(self.cal.sub(a,b),2)
        assert expect==result_sub



    # @pytest.mark.parametrize('a,b,expect',[
    #     (1.5,0.6,0.9),
    #     (5,6,30),
    #     (-1,-5,5)
    # ],ids=['浮点数','正数','负数'])
    @pytest.mark.parametrize('a,b,expect',getdatas.test_get_muldatas()[0],ids=getdatas.test_get_muldatas()[1])
    def test_mul(self,a,b,expect):
        result_mul = round(self.cal.mul(a,b),2)
        assert expect==result_mul

    # @pytest.mark.parametrize('a,b,expect',[
    #     (1.5,0.6,2.5),
    #     (5,6,0.83),
    #     (-1,-5,0.2)
    # ],ids=['浮点数','正数','负数'])
    @pytest.mark.parametrize('a,b,expect', getdatas.test_get_divdatas()[0], ids=getdatas.test_get_divdatas()[1])
    def test_div(self,a,b,expect):
        result_div = round(self.cal.div(a,b),2)
        assert expect==result_div
