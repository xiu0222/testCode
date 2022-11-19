# post
# url = 接口地址/json=参数(字典格式)、hearders=请求头(字典格式)
import requests
from dbtools import query

url = "http://118.24.105.78:2333/login"
data = {"username":"liuyun1","password":"a12345678"}
h = {"Content-Type":"application/json"}

res = requests.post(url=url,json=data,hearders=h)
assert res.status_code ==200
assert res.json9()["status"] == 200

sql ="select * from t_user where username = 'liuyun1'"
assert len(query(sql)) != 0
print("接口测试成功")

token = res.json()["date"]["token"]

url1 = "http://118.24.105.78.2333/inspirer/new"
header1 ={"Content-Type":"application/json","token":token}
data1 ={"content":"这是来自星星的数据","xing":"dsfsdf.jpg"}
res1 =requests.post(url=url1,json=data1,headers=header1)
print(res1,text)



