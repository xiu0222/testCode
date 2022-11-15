"""
类   Class person


"""# 成员变量：类中的变量

class Person():
    # 成员变量：类中的变量
    name = "小明"
    age = 18
    sex = "男"

    #成员方法：类中的方法
    def eat(self,a1):
        print("人能吃东西{}".format(a1))   # 只是为了演示
        return"xxx"

    def run(self):   
        self.aihao = "女"     #初始化成员变量
        self.name = "小张"    #  替换成员变量的值
        print("这个类的名字是{}".format(self.name))

    def test(self):
        self.run()

    #调用类：实例化类：------P实例化对象，类的把柄
P = Person()
# print(P.name)
# P.eat()      #self参数一定不要传
# a =P.eat("海鲜")
# print(a)
# P.run()
# print(P.aihao)
# print(P.name)
P.test

