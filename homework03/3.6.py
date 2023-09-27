score=int(input())
if(score>=90 and score<=100):
    print("等级为：优秀")
elif(score>=75 and score<90):
    print("等级为：良好")
elif(score>=60 and score<75):
    print("等级为：合格")
elif(score>=0 and score<60):
    print("等级为：不合格")
else:
    print("分数输入错误！")