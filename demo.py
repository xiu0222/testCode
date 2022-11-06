"""
python的常见方法:any
print("hello你好,这是小讲堂")
print("哈哈",end="1111")
print(678)
print(8.98)
print(True,False)
print(None)
print(())
print([])
print({})



print("haha"+"西西")
print("哈哈"*100)
print(1+1)
print(1+5*2/(2+4))
print(10//3)
print(10/3)
print(10%6)
print(1>0 and 4>3)
print(1-1==0 or 2<1)

name = "张三"
print(name)
# 把张三这个值赋值给name
单行注释快捷键是ctrl+/

res =1+2+3+4
print(res)

a = input("请输入：")
print("这是我刚输入的值：",a)

a = len("哈哈哈哈哈哈哈哈哈哈")
print(a)
"""

b = ("刘巧云","欧阳")
a = (1,2,3,4,"哈哈","希希",True,None,b)

"""
元组内什么都可以放
这样可以少些几个变量
# 每个变量都占用计算机内存，变量越多，占用的内存就越多
下标是计算机自动给我们的值编的号，是从0开始
index是获取某值的下标
count是获取某值的下标个数只针对一维元组可用
index和count

# print(a[3])
# print(a[-4])

print(a.index("哈哈")) 
print(a.count(1))
# 这里的a是一个元组
#二维元组 ，三维元组
求二维元组的下标，首先定位到二维元组，再写出对应元组的下标
比如欧阳；print(a[-1].index("欧阳"))


切片：左闭右开   如a[1:3]从下标0到下标3
print(a[0:4])

# 把欧阳取出来
# print(a[-1][-1])


# 数组
# a = []
"""
b = ("刘巧云","欧阳","马超")
a = [1,2,3,4,"哈哈","希希",True,None,b]
print(a)


"""
元组和数组的操作方式一模一样
区别是元组不可以修改，数组可以修改



数组 [] 的方法：
index       获取某个值的下标
count       获取某个下标值的个数
append      往数组中追加内容
insert      往数组中的指定位置插入数据（配合下标使用）
pop         从数据中取走数据（通过下标来操作）
extend      合并数据
sort        排序
remove      删除某个值,里面填的是值
clear       清空
resvers     颠倒/倒序，和排序一起用


name = input("请输入名字：")
a.append(name)
a.insert(3,name)
print(a)


# name = input("请输入名字：")
# a.append(name)
# a.insert(3,name)
# # xx = a.pop(5)
# # print(xx)
# print(a)
"""

c = ["今天","明天","后天"]


"""
# # a.extend(c)
# a = a + c
# print(a+c)
"""



d = [4,5,7,9,2,"哈哈","哈哈"]
# d.sort(reverse=True) 
# d.reverse
# d.clear()
print(d)
d.remove("哈哈")
print(d) 







 



