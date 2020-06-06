# num = int(input('请输入一个数字:'))
# jc=1
#  
# if num < 0 :
#     print('抱歉负数没有阶乘')
# elif num == 0 :
#     print('0的阶乘为1')
# else:
# 
# 
#     for i in range(1,num+1):
#        
# 
#         jc = jc*i
#     
# 
# 
# 
# print(jc)
list= [1,22,3,4,5,6,7]
# for i in list :
#     for j in list [list.index(i)+1:] :
#         print(i,j)
# 
# 
# for i in list:
#     for j in list [list.index(i)+1:] ：
#         print(i,j)

for i in list :
    for j in list[list.index(i)+1 :] :
        if i +j ==4:
            print(list.index(i),list.index(j))


