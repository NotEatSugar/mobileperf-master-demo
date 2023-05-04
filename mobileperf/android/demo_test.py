# encoding: utf-8
# 时间 2022/11/1 18:00

# for item in range(100,1000):
#     # 输出100-999的水仙花数 例如153 = 3*3*3+5*5*5+1*1*1
#     ge = item % 10  #获取各位数
#     shi = item//10 % 10  #十位
#     bai = item//100   #百位
#     if ge**3+shi**3+bai**3==item:
#         print(item)

# for item in range(3):
#     pwd = input("请输入密码")
#     if pwd =="888":
#         print("密码正确")
#         break
#     print("密码错误")
# else:
#     print("输入密码次数用完了")
import re
import win32com.client

a = 0
# while a <3:
#     pwd = input("请输入密码")
#     if pwd =="888":
#         print ("密码正确")
#         break
#     else:
#         print("密码错误")
#     # if a ==2:
#     #     print("输入次数用完了")
#     a+=1
# else:
#     print("输入次数用完了")


# for item in range(1,51):
#     # 输出1-55之间所有5的倍数 分析 5的倍数的除5的余数为0都是5的倍数
#     if item % 5 !=0:
#         continue
#     else:
#         print(item)
#  # 输出一个3行4列的矩形
# for i in range(1, 4):
#     for x in range(4):
#         print(x,end="\t") # 不换行输出
#     print() # 执行完成后换行
#  打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s" %(i,j,i*j),end="\t")
#     print()lst
# lst = [30, 11, 1.2]
#
# lst2= [i*i for i in range(1,11)]
# print(lst2)
# a = 1
# pattern = re.compile(r'([\w|\-|\.]+):(.+)')
# if not a :
#     print("打印")
speaker = win32com.client.Dispatch('SAPI.SpVoice')

speaker.Speak('爱你哟~爱你呦~爱你呦~，我只是嘴甜，我心里没你')

