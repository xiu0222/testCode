# 字典{}

a = {"name":"张三"}
print(a)


"""
字典没有下标的概念
说明字典没有顺序的说法
字典取值,靠key
"""
# 取值
print(a["name"])           #当key不存在时,报错
print(a.get("name1"))      #当key不存在时,返回空

#新增和修改
a["name"] = "成都"     #当key不存在时,新增；当key不存在时，就修改
a.update(address="王二")  #update的写法的时候，key在这里是一个变量的写法
print(a)


#取走
a.pop("name")

#通用的删除方法，可以删字典，也可以删数组
# del a["name"]
#print(a)

print(a.keys())   
print(list(a.keys()) )

print(list(a.values()))