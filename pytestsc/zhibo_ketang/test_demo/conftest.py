from typing import List

#conftest.py文件添加如下代码即可修改测试结果的编码格式，如中文展示
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')