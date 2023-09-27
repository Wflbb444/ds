import math
# 辗转相除法
def fuc(n, m):
    temp = n % m
    while temp != 0:
        n = m
        m = temp
        temp = n % m
    return m
a,b=input().split(" ")

if(a.isdigit()==False or b.isdigit()==False or int(a)<=0 or int(b)<=0):
    print("请输入两个正整数！")
else:
    gcd=fuc(int(a),int(b))
    print("最大公约数为:",end="")
    print(gcd)