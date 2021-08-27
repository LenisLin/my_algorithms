##### 04_quicksort
import random
import time
## eg1：数组求和的两种方法
## 方法1：直接循环
def sum1(arr):
    total=0
    for i in range(0,len(arr)):
        total=total+arr[i]
    return total

## 方法2：递归
def sum2(arr,total):
    if(len(arr)==0): ## 收敛条件
        return total
    else: ## 递归条件
        total=total+arr.pop(0)
        return sum(arr,total)

total=0
arr=[1,3,4,5,6]
print(sum1(arr))
print(sum2(arr,total))

## eg2：数组长度统计
## 方法1：循环
## 方法2：递归
length=0
def count2(arr,length):
    if(arr==[]):
        return length
    else:
        length=length+1
        return count2(arr[1:],length)
print(count2(arr,length))
print(len(arr))

## eg3：求最值
## 方法1：利用循环O（n）复杂度
## 方法2：利用递归
def max2(arr):
    if(arr==[]):
        return None
    elif(len(arr)==1):
        return arr[0]
    else:
        if(arr[0]>arr[1]):
            arr.pop(1)
            return max2(arr)
        else:
            arr.pop(0)
            return max2(arr)
        ## return max(arr[0],max2(arr[1:])) ## 直接用递推公式写

arr=[1,3,5,2,3,4,2,3,9,0]
print(max2(arr))

## commence
## 对于这些可以利用D&C思路解决的问题，我们都需要去确定它的收敛条件和递归条件。
## eg4：快速排序
def quicksort(arr):
    if(len(arr)<2): ## 收敛条件，当数组长度为0或者1的时候就不需要继续排序了
        return arr
    else:
        pivot=arr[0] ## 选取主元，这里是把数组的第一个作为主元

        less=[i for i in arr[1:] if i<pivot] ## 把数组中小于主元的生成一个列表
        greater=[i for i in arr[1:] if i>pivot] ## 把数组中大于主元的生成一个列表

        return quicksort(less)+[pivot]+quicksort(greater) ## 局部快排

arr=[10, 5, 2, 3]
print(quicksort(arr))

## LeetCode 912：排序数组
## 给你一个整数数组 nums，请你将该数组升序排列。
class Solution: ## 快速排序，时间复杂度平均O（log n·）
    def sortArray(self, nums):
        import random
        def quicksort(arr):
            if (len(arr) < 2):  ## 收敛条件，当数组长度为0或者1的时候就不需要继续排序了
                return arr
            else:
                pivot = arr[0]  ## 选取主元，这里是把数组的第一个作为主元，这是很关键的一步，决定我们的复杂度
                less = [i for i in arr[1:] if i < pivot]  ## 把数组中小于主元的生成一个列表
                greater = [i for i in arr[1:] if i >= pivot]  ## 把数组中大于主元的生成一个列表

                return quicksort(less) + [pivot] + quicksort(greater)  ## 局部快排
        return quicksort(nums)
nums = [5,1,1,2,0,0]
print(Solution().sortArray(nums))

## 对上面的快速排序进行改进：①主元选取采用随机数的方法来选取，②当元素个数少于100个的时候采用插入排序
class Solution:
    def sortArray(self, nums):
        def insert_sort(arr):
            if (arr == []):
                return []
            elif (len(arr) == 1):
                return arr
            else:
                new_arr = []
                length = len(arr)
                for j in range(0, length):
                    minium = arr[0]
                    for i in arr:
                        if (i <= minium):
                            minium = i
                        else:
                            continue
                    new_arr.append(minium)
                    arr.remove(minium)
                return new_arr

        def quick_sort(arr):
            if (len(arr) < 100):
                return insert_sort(arr)
            else:
                pivot = random.choice(arr[1:99])
                arr.remove(pivot)
                less = [i for i in arr if i < pivot]
                greater = [i for i in arr if i >= pivot]

                return quick_sort(less) + [pivot] + quick_sort(greater)
        return quick_sort(nums)

## get test arr
import random
def get_test_arr(length):
    test_list=[]
    while(len(test_list)<length):
        test_list.append(random.randint(-5000,5000))
    return test_list
arr=get_test_arr(random.randint(1,5000))
arr=[-4,0,7,4,9,-5,-1,0,-7,-1]
print(Solution().sortArray(arr))

