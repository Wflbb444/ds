#选择排序，时间复杂度为O(n^2)
import random

def selection_sort(num_list):
    length = len(num_list)
    if length <= 1:
        return num_list

    for j in range(length):
        # 假设第一个元素为最小元素
        min_num_index = j
        
        # 遍历未排序区域元素，以此和未排序区域的第一个元素做对比
        for i in range(j+1, length):
            if num_list[i] < num_list[min_num_index]:
                min_num_index = i
         
        # 交换位置
        num_list[min_num_index], num_list[j] = num_list[j], num_list[min_num_index]

    return num_list
random_list1 = random.sample(range(100), 10)
print(random_list1)
selection_sort(random_list1)
print(random_list1)
print("\n")
random_list2 = random.sample(range(100), 50)
print(random_list2)
selection_sort(random_list2)
print(random_list2)
print("\n")
random_list3 = random.sample(range(1000), 100)
print(random_list3)
selection_sort(random_list3)
print(random_list3)