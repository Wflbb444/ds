
import numpy as np
def f(x):
  return x**2 + 4*x*np.sin(x) 
def intf(x): 
  return x**3/3.0+4.0*np.sin(x) - 4.0*x*np.cos(x)
a = 2;  
b = 3; 
# use N draws 
N= 10000
X = np.random.uniform(low=a, high=b, size=N) # N values uniformly drawn from a to b 
Y =f(X)  # CALCULATE THE f(x) 
# 蒙特卡洛法计算定积分：面积=宽度*平均高度
Imc= (b-a) * np.sum(Y)/ N
exactval=intf(b)-intf(a)
print("Monte Carlo estimation=",Imc, "Exact number=", intf(b)-intf(a))
