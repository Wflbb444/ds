#开平方1
import math
def Square_root_1():
    c=2
    i=0
    g=0
    for j in range(0,c+1):
        if(j*j>c and g==0):
            g=j-1
    while(abs(g*g-c)>0.0001):    
        g+=0.00001       
        i+=1
        print("%d:g=%.5f"%(i,g))
Square_root_1()