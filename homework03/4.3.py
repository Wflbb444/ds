def insertion_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i - 1, -1, -1):
            if(lst[j] > lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]                
list1 = [6,5,3,1,8,7,2,4]
insertion_sort(list1)
print(f"排序结果：{list1}")