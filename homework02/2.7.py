#c的三次方根的牛顿迭代式
def Square_root_3():
    c=10
    g=c/2
    i=0
    while(abs(g*g*g-c)>0.00000000001):
        g=(2*g+c/(g*g))/3
        i=i+1
        print("%d:%.13f"%(i,g))
Square_root_3()