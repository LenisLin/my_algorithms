##### 01_introduction_to_algorithms
## binary searching
def binary_search(list,item):
    ## 二分查找：传入一个列表（保证这个列表是有序的），找到某个元素对应的下标，如果不存在则返回-1
    ## 这里以找数字为例子

    ## 先定义最左边的index和最右边的index
    left=0
    right=len(list)
    if (left>=right):
        return -1

    ## 循环条件是左边界仍然小于右边界
    else:
        while(left<right):
            mid=(left+right)//2
            if(list[mid]>item): ## 意味着中间的值偏大
                right=mid-1
            if(list[mid]<item): ##意味着中间的值偏小
                left=mid+1
            if(list[mid]==item): ## 中间的记为所求
                return mid
            ## 如果上面不设置成mid-1或者mid+1，则会陷入死循环
        return -1

## test
import json
with open("G:/project/grokking_algorithms/01_introduction_to_algorithms/python/items.json", "r") as file:
  data = json.load(file)
print(data.items())
simple_list = data["simple_list"]
list_with_10_items = data["list_with_10_items"]
list_with_100_items = data["list_with_100_items"]
list_with_1000_items = data["list_with_1000_items"]

print(binary_search(list_with_100_items,149))

## LeetCode example
## LeetCode 4：寻找两个正序数组的中位数
## 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

## 解题思路：
## 总体上分成两步：1.整合成一个新的有序数组 2.找到这个数组的中位数

## 完整的代码
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums_finally = list()

        while(True):
            if(len(nums1)!=0 and len(nums2)!=0):
                if(nums1[0]>nums2[0]):
                    nums_finally.append(nums2.pop(0))
                elif(nums1[0]<nums2[0]):
                    nums_finally.append(nums1.pop(0))
                else:
                    nums_finally.append(nums1.pop(0))
                    nums_finally.append(nums2.pop(0))
            elif(len(nums1)!=0 and len(nums2)==0):
                nums_finally=nums_finally+nums1
                break
            elif(len(nums2)!=0 and len(nums1)==0):
                nums_finally = nums_finally + nums2
                break
            else:
                break
        ## 获取中位数
        length=len(nums_finally)
        if(length%2==1):
            return nums_finally[((length-1)//2)]
        else:
            return (nums_finally[(length)//2]+nums_finally[(((length)//2)-1)])/2

## example
nums1=[1,1]
nums2=[1,2]
print(Solution().findMedianSortedArrays(nums1,nums2))

## LeetCode 704：二分查找
## 给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1
class Solution:
    def search(self, nums, target):
        if(target>nums[len(nums)-1] or target<nums[0]):
            return -1
        else:
            left=0
            right=len(nums)

            while(True):
                if(left>right):
                    return -1
                else:
                    mid=(left+right)//2
                    if(nums[mid]>target):
                        right=mid-1
                    elif(nums[mid]<target):
                        left=mid+1
                    else:
                        return mid
## test 1
nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums,target))

## test 2
nums = [-1,0,3,5,9,12]
target = 2
print(Solution().search(nums,target))

## test 3
nums = [-1,0,3,5,9,12]
target = 13
print(Solution().search(nums,target))

