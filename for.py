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


# range [0,1,2,3,4,5,6,7,8,9]
a = ["李虎","都督","古巴","欧巴","都司","王","刘","蔡","马","董"]
for i in range(len(a)):   #len(a) = 10;range(10)>[0,1,2,3,4,5,6,7,8,9]
    print(a[i])#len(a)代表a里有多少个元素，range（len(a)）是下标算法
    