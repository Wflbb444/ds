(1)# 动态规划
# 1.定义子问题
# dp[i]是正整数列的最大乘积
# 2.递推关系
# dp[i]：当i>=2时
# (1)dp[i]=j*(i-j)(不再拆分)
# (2)dp[i]=j*dp[i-j](还需拆分)
# 3.初始值
# dp[0]=dp[1]=0
# import math
# n=int(input())
# dp=[0]*(n+1)
# dp[0]=0
# dp[1]=0
# dp[2]=1
# for i in range(3,n+1):
#     for j in range(i-1,0,-1):
#         dp[i]=max(dp[i],max((i-j)*j,dp[j]*(i-j)))
# print(dp[n])
# 答：正整数列为667个3

# (2)数学方法：
# 求函数y=(n/x)^x(x>0)的最大值，可得x=e时y最大，分解成整数，所所以x取2或3，
# 又因为2^3=8<9=3^2，所以应分解为多个3
n=int(input())
if n==2:
    ans=[1]
elif n==3:
    ans=[1,2]
elif n==4:
    ans=[2,2]
else:
    if n%3==0:
        ans=[3]*int(n/3)
    elif n%3==1:
        ans=[3]*int(n/3-1)
        ans.append(2)
        ans.append(2)
    else:
        ans=[3]*int(n/3)
        ans.append(2)
print(ans)