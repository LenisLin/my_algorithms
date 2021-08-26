##### 02_selection_sort
## selection sort O(n^2)
def find_smallest(nums):
    if(len(nums)==0):
        return
    elif(len(nums)==1):
        return 0
    else:
        smallest=nums[0]
        index=0
        for i in range(1,len(nums)):
            if(nums[i]<smallest):
                index=i
                smallest=nums[i]
            else:
                continue
        return index

def selection_sort(nums):
    new_nums=list()
    for i in range(0,len(nums)):
        new_nums.append(nums.pop(find_smallest(nums)))
    return new_nums

nums = [5,2,3,1]
print(selection_sort(nums))

## LeetCode 912：排序数组
## 给你一个整数数组 nums，请你将该数组升序排列。
class Solution:
    def sortArray(self, nums):
        def find_smallest(nums):
            if (len(nums) == 0):
                return
            elif (len(nums) == 1):
                return 0
            else:
                smallest = nums[0]
                index = 0
                for i in range(1, len(nums)):
                    if (nums[i] < smallest):
                        index = i
                        smallest = nums[i]
                    else:
                        continue
                return index

        new_nums = list()
        for i in range(0, len(nums)):
            new_nums.append(nums.pop(find_smallest(nums)))
        return new_nums

## test
nums = [0,0]
print(Solution().sortArray(nums))