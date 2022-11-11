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
    a = query(sql)
    print(a) 




"""






sql = "selsct * from t_goods where goods = 'iphone12'"
res = query(sql)
if res [0][2] >5488:
    print("打扰了，我选华为 ")
else:
    print("我爱华为，我选苹果")
    