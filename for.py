#循环
"""
# chengji = [80,90,59,49,28,]
# for i in chengji:
#     if i < 60 :  for的in去取值
#         print("发现一个壮士，成绩是{}".format(i))
"""

"""
chengji = [80,90,59,49,28,]
for i in chengji:
    if i < 60 :
        print(i)
"""


"""
# 遍历数组

#把成绩合格的添加到一个list中,不合格的添加到另一个list中
chengji = [80,90,59,49,28,]
hege = []
nohege =[]
for i in chengji:
    if i < 60 :
        hege.append(i)
    else:
        nohege.append(i)
print(hege)
print(nohege)
"""
"""
#遍历字典
zhanghao ={"username":"王美丽","chengji":88}
# for i in zhanghao:
#     print(i)
#     print(zhanghao.get(i))
"""

"""
# 遍历字典中的key值
zhanghao ={"username":"王美丽","chengji":88}
for i in zhanghao.keys():
    print(i)
"""

"""
# 遍历字典中的valus值:
zhanghao ={"username":"王美丽","chengji":88}
for i in zhanghao.values():
    print(i)

"""

"""
zhanghao ={"username":"王美丽","chengji":88} 
for i,j in zhanghao.items():
    print(i)
    print(j)
"""


#遍历字符串
# a = "你好漂亮！"
# for i in a :
#     print(a)

"""
range()   序列生成器(固定用法,range里只能用数字)
"""

"""
# range [0,1,2,3,4,5,6,7,8,9]
a = ["李虎","都督","古巴","欧巴","都司","王","刘","蔡","马","董"]
for i in range(len(a)):   #len(a) = 10;range(10)>[0,1,2,3,4,5,6,7,8,9]
    print(a[i])#len(a)代表a里有多少个元素,range(len(a)）是下标算法
"""

#进阶
# a = [[1,2,3],[4,5,6]]
# for i in a:
#     for j in i:
#         print(j)


"""
b =[{"username":"郭子","passward":"123456"},{"username":"小玉","passward":"123456"}]
for i in b:#{"username":"郭子","passward":"123456"}j1=username,j2=passward
    for j in i:#{"username":"小玉","passward":"123456"}j1=username,j2=passward
        # print(i)        
        print(j)
        print(i[j])
"""

#用for循环实现用户登录：t_user是数据的表
t_user = {"username":"郭子","passward":"123456"},{"username":"小玉","passward":"123456"}
u = input("请输入账号:")
p = input("请输入密码:")
a = 1
for i in t_user:
    if u == i.get("username") and p == i.get("passward"):
        print("登陆成功")
        break   #终止循环
    else:
        # 最后一次运行还没有这个账号：再来打印登陆失败
        # 怎么判断是最后一次
        if len(t_user) == a:
            print("登陆失败 ")

    a = a + 1

# 什么算法，怎么实现出来
# 请用python写出a列表中的重复元素的下标和值

a = ["张","胡","王","夏","张","李"]
for i in range(len(a)) :
    if a[i] ==  a[i+1]:
     print(i)
    






# 排序：请用python对a列表进行从小到大的排序
a = [1,2,3,555,666,777,-1]






