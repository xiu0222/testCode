"""
# import pymysql  # 想要用朋友MySQL,就必须要导入它



def query(sql):
    # 固定的方法
    #    db = pymysql.connect(host='ip地址',user='账号',password="密码 ",db='数据库名字') 
    db = pymysql.connect(host='192.144.148.91',user='ljtest',password="lj123456+",db='ljtest') 
query("123")
#获取查询窗口，游标： 
    cur = db.cursor()
#执行SQL语句
    cur.execute(sql)
#获取所有的结果
    res = cur.fetchall()
    db.close()
    return res



if _name_ = "_main_":
    # sql = "select * from t_user where username ='liuyun'"
    sql ="select * from t_pymysql_account wherer username = 'python'"
   #更换数据表格时,直接改sql语句就行
    a = query(sql)
    print(a) 

#结果出来((列1),(列2),(列3),)
#返回结果是元组,返回的值中,有逗号时,是tuple格式,如果没有最后的逗号,那就是int格式.


"""




# 用python查询商品t_goods表里的商品名为iphone的价格,并且判断价格如果大于5488,则显示买不起,否则显示买买买

sql = "selsct * from t_goods where goods = 'iphone12'"
res = query(sql)
if res [0][2] >5488:
    print("打扰了，我选华为 ")
else:
    print("我爱华为，我选苹果")
    