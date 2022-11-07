 

#  while的固定格式:
"""
a = 10
while a >0:
    print(a)
    a = a - 1

while:重复的执行某个相同的代码，循环
      条件不满足时就退出循环

a = 10 ; > 10 ;a = 10 - 1 > 9
a = 9  ; > 9  ;a = 9 - 1 > 8
a = 8  ; > 8  ;a = 8 - 1 > 7
a = 7  ; > 7  ;a = 7 - 1 > 6
a = 6  ; > 6  ;a = 6 - 1 > 5
a = 5  ; > 5  ;a = 5 - 1 > 4  
a = 4  ; > 4  ;a = 4 - 1 > 3
a = 3  ; > 3  ;a = 3 - 1 > 2
a = 2  ; > 2  ;a = 2 - 1 > 1
a = 1  ; > 1  ;a = 1 - 1 = 0
a  = 0  :条件不满足时,就不执行whlie
"""

# 有个list[80,90,59,49,28,87,99]来判断成绩是否合格，不合格的打印出来
   

a = 0 # chengji的下标
chengji = [80,90,59,49,28,]
while a < 5 :    #或者5也可以用len（chengji） #如何准确地获取到列表中每个元素而不落下
    if(chengji[a])<60:   #下标和运行次数的关系
       print("发现一个壮士，成绩是{}".format(chengji[a]))
        
    a = a + 1





"""
a = 0 # chengji的下标
res = ""
chengji = [80,90,59,49,28,]
while a < 5 :    #或者5也可以用len（chengji） #如何准确地获取到列表中每个元素而不落下
    if(chengji[a])<60:   #下标和运行次数的关系
    #    print("发现一个壮士，成绩是{}".format(chengji[a]))
        res = res + "," + str(chengji[a])
    a = a + 1

print("发现一个壮士，成绩是："+res)
"""
