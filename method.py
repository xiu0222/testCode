
"""
# 练习自定义一个减法方法/函数，要求去调用这个方法,显示返回值
def add(s1,s2):
     sum=s1-s2
     return sum



a = add(6,2)
b = add(8,5)
print(a)
print(b)

"""

def login(username,password):

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

u = input("请输入账号：")
p = input("请输入密码：")
login(u,p)


