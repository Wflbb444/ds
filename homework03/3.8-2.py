#归并排序，时间复杂度为O(nlog2 N)
import random

def merge(left, right):
    ll, rr = 0, 0
    result = []
    while ll < len(left) and rr < len(right):
        if left[ll] < right[rr]:
            result.append(left[ll])
            ll += 1
        else:
            result.append(right[rr])
            rr += 1
    result+=left[ll:]
    result+=right[rr:]
    return result

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    num = len(alist) // 2   # 从中间划分两个子序列
    left = merge_sort(alist[:num]) # 对左侧子序列进行递归排序
    right = merge_sort(alist[num:]) # 对右侧子序列进行递归排序
    return merge(left, right) #归并
random_list1 = random.sample(range(100), 10)
print(random_list1)
merge_sort(random_list1)
print(random_list1)
print("\n")
random_list2 = random.sample(range(100), 50)
print(random_list2)
merge_sort(random_list2)
print(random_list2)
print("\n")
random_list3 = random.sample(range(1000), 100)
print(random_list3)
merge_sort(random_list3)
print(random_list3)