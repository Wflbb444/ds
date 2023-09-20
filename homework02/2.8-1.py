#圆周率计算公式法，梅钦级数，效率最高
 
pi=0
N=eval(input())
 
for k in range(N):
    pi+=1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
 
print(pi)