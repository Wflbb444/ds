#性能最慢
from random import *
seed(100)     #设定种子以固定随机数
 
dot=0
dots=eval(input('请输入您想填充的点数：')) 
 
for i in range(1,dots+1):
    x,y=random(),random()
    r=pow(x**2+y**2,0.5)
    if r<=1:
        dot+=1
pi=4*(dot/dots)
print('所得圆周率为：{}'.format(pi))