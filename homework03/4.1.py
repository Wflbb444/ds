import math
number = int(input('请输入数字:'))
if(number==1):
    print("1不是质数")
elif(number<=0):
    print("请输入正整数！")
else:
#标志 flag为0 表示：是质数； flag为1 表示：不是质数
    flag = 0
#循环
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            flag = 1
    if flag == 0:
        print(number, '是质数')
    else:
        print(number, '不是质数')

