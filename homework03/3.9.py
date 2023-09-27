import random
listA = random.sample(range(1,11), 10)
listB=[]
for i in range(0,10):
    b=1
    for j in range(0,i):
        b*=listA[j]
    for j in range(i+1,10):
        b*=listA[j]
    listB.append(b)
print(listA)
print(listB)