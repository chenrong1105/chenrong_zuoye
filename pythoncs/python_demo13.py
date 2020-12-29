'''yaml文件处理
yaml注意事项：
1.大小写敏感
2.key:value格式的数据，key:后一定要加个空格
3.不可使用tab键进行缩进，只可以使用空格缩进
4.yaml支持列表、字典、字符串等值
'''
import yaml

with open("b/demo3.yaml","w") as f: #将转化后的yaml格式数据写入到demo3.yaml文件
    yaml.dump(data={"a":[1,2]},stream=f)#yaml.dump()将Python数据格式转化为yaml格式

print(yaml.load(open("b/demo3.yaml")))#yaml.load()将指定的yaml文件内容转化为python数据格式