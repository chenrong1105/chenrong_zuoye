import pytest
#多种组合测试数据
@pytest.mark.parametrize("a",[1,5,3])
@pytest.mark.parametrize("b",[5,7,8,'m','n'])
def test_para(a,b):
    print(f"a={a},b={b}")