import pytest
import requests
import selenium
import appium

'''第三方库的使用,需要先对第三方库进行安装：pip install requests'''
r=requests.get("http://www.baidu.com")
print(r.status_code)
r.encoding="utf-8"
print(r.text)

r1=requests.post("http://www.baidu.com",data={"key":"value"})
print(r1.text)
