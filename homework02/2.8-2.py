#割圆迭代法，效率中等
import math
n=6
a=1
print("%-15s%-20s" % ("内接正n边形","π计算结果"))
print("%-20d%-20.12f" % (n, n*a/2))
for i in range(14) :
  n=2*n
  a=math.sqrt(2-2*math.sqrt(1-(a/2)**2))
  print("%-20d%-20.12f" % (n, n*a/2))