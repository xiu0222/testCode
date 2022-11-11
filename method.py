
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
        print('这是第{}次运行,i的值是{}'.format(a,i))
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



"""
metheod方法:
1.def 方法名字（参数）:
(1).命令:add_sth_and_sth2
(2).参数:1).参数可选，也可只有一个
     2).方法定义了几个参数，就传几个参数，没有定义参数不传
     3).可以有默认值
     4).传参的时候给指定参数的值
     5).参数可传任意数据类型
2.return:返回值
        返回值可选


pymysql
1.python连接中断并且操作MySQL的第三方包(第三方包:连接并且操作MySQL的第三方包)
2.环境搭建:
        pip,python自带的第三方包管理工具(cmd中输入pip、以及pip -V检验是否安装好)
        pip install mysql -i https://pypi.tuna.tsinghua.edu.cn/simple(管理员端输入)
3.学习:
      (1).知道咋用，知道咋改
      (2)弄清楚python连接mysql的步骤(mysql的方法都是固定的)
4.学习步骤:
        连接数据库:host="连哪个服务器的IP"
                  user="数据库名称"
                  passwor="账号的密码"
                  db="要打开的数据据库名字"
5.sql的注意事项:
            (1).字符串类型
            (2).字符串符号原则：外双内单,外单内双
            (3).拼接sql的字符串    {}.format
            (4).换数据表就改变sql语句


def add(s1,s2):




"""