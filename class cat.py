"""
类的继承:好处:
子类可以继承父类的属性和方法
子类可以重写父类的属性和方法
Son:子类
Baba:父类
"""


class cat():
    #构造方法：固定方法，类实例化的时候运行
    def __init__(self,mx,nl):
        self.name = mx
        self.age = nl



    def aa(self):
        a = 1 #只针对aa有效
        self.b =2 #整个类都有效



#一定要加参数
c = cat("tomcat",18)
print(c.name)
c.aa()
print(c.b)
