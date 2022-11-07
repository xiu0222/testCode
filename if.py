#进阶
#2.输入一个账号，输入一个密码，要求判断账号的长度大于5位，并且小于8位，
#如果输入账号为张三12345，密码为123456就可以登陆成功，否则就登录失败


zh = input("请输入zh:")
mm = input("请输入密码：")
if len(zh)>5 and len(zh)<8:
    print("账号长度合法")
    if zh =="张三12345" and mm =="123456":
        print("登陆成功")
    else:
        print("登陆失败，账号或密码错误")
else:
    print("账号长度不合法")


"""
shift + TAB 向前一个单元格
TAB   向后一个单元格
ctrl + s 是保存
CTRL + TAB 文件之间切换
CTRL + X   剪切当前行
CTRL + shift + K 删除当前行
ctrl + B 侧边栏显示或隐藏
CTRL + ~ 调出终端
CTRL + SHIFT + W 关闭当前的VScode编辑器
CTRL + w 关闭当前窗口   
"""