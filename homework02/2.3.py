N = 15
a = [[0] * 4 for i in range(N)]
b = [0] * N
name = [" ",
"and 狼",
"and 羊",
"and 菜"]
def search(Step):
    # 若该步骤能使各值均为1，则输出结果
    if a[Step][0] + a[Step][1] + a[Step][2] + a[Step][3] == 4:
        for i in range(Step + 1):
            print('原岸:', end=' ')
            if a[i][0] == 0:
                print('狼', end=' ')
            if a[i][1] == 0:
                print('羊', end=' ')
            if a[i][2] == 0:
                print('菜', end=' ')
            if a[i][3] == 0:
                print('人', end=' ')
            if a[i][0] and a[i][1] and a[i][2] and a[i][3]:
                print("空", end='')
            print(end=' ')
            print('对岸:', end=' ')
            if a[i][0] == 1:
                print("狼", end=' ')
            if a[i][1] == 1:
                print('羊', end=' ')
            if a[i][2] == 1:
                print('菜', end=' ')
            if a[i][3] == 1:
                print('人', end=' ')
            if not (a[i][0] or a[i][1] or a[i][2] or a[i][3]):
                print('空', end='')
            if i < Step:
                print(' 第 %d 次' % (i + 1))
            if i>0 and i<Step:
                if a[i][3] == 0: # 人在本岸
                    print(" -----> 人 ", end='')
                    print(name[b[i] + 1])
                else: # 人在对岸
                    print(" <----- 人 ", end='')
                    print(name[b[i] + 1])
        print('\n\n')
        return
    for i in range(Step):
        # 若该步与以前的步骤相同，取消操作
        if a[i] == a[Step]: 
            return
    # 若羊和人不在一起而狼和羊或者羊和白菜在一起，则取消操作
    if a[Step][1] != a[Step][3] and (a[Step][2] == a[Step][1] or a[Step][0] == a[Step][1]):
        return
    # 递归，从带第一种对象开始依次向下循环
    for i in range(-1, 3):
        b[Step] = i # 记录人渡河的方式
        a[Step+1] = a[Step][:] # 复制上一步的状态，进行下一步移动
        a[Step + 1][3] = 1 - a[Step + 1][3] # 人过去或者回来
        if i == -1:
            search(Step + 1) # 第一步
        elif a[Step][i] == a[Step][3]: # 若物与人同岸，带回
            a[Step + 1][i] = a[Step + 1][3] # 带回该物
            search(Step + 1) #下一步
print(' 渡河问题解决方案：\n')
search(0)