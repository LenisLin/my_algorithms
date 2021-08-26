##### 03_recursion
## 3.2：基线条件和递归条件
def cutdowm(i):
    print(i)
    if (i <= 0): ## 基线条件
        return
    else: ## 递归条件（调用自己）
        cutdowm(i)
## 3.3.1：调用栈
## 栈这种数据结构是实现递归的方法
def greet(name):
    print("hello, "+name+" !")
    greet2(name)
    print("getting ready to say bye...")
    bye()
def greet2(name):
    print("how are you, "+name+" ?")
def bye():
    print("OK bye!")

greet("Lin") ## 使用greet函数时，先调用greet，发现要先调用greet2，把它暂时压入堆栈，调用greet2，然后顺序调用bye,最后把栈里面的greet执行掉。

## 3.3.2：递归调用栈
def fact(x):
    if(x==1): ## 基线条件（收敛条件）
        return 1
    else: ## 递归条件
        return x*fact(x-1)
print(fact(5))

## 编写一个递归程序：
# ①找到收敛条件（边界值）
# ②递归条件（写成类似数列递推公式的形式）
# ③根据需要转化成时间复杂度更低的循环

## LeetCode 231：2的幂
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
# 如果存在一个整数 x 使得n == 2^x ，则认为 n 是 2 的幂次方。

### 思路1：利用递归解决
def find_n(x,n):
    if(x>=n):
        return x
    else:
        return find_n(x*2,n)

x=1
print(find_n(x,3))

class Solution:
    def isPowerOfTwo(self, n):
        if(n<=0):
            return False
        else:
            x=1
            def find_n(x, n):
                if (x >= n):
                    return x
                else:
                    return find_n(x * 2, n)
            if(n==find_n(x,n)):
                return True
            else:
                return False

n=8
print(Solution().isPowerOfTwo(n))

### 思路2：利用循环解决
class Solution2:
    def isPowerOfTwo2(self, n):
        if(n<=0):
            return False
        else:
            def find_n2(n):
                x = 1
                while (True):
                    if (x >= n):
                        return x
                    else:
                        x = x * 2
            x=find_n2(n)
            if(x==n):
                return True
            else:
                return False
n=8
print(Solution2().isPowerOfTwo2(n))

## 4.1 分而治之（D&C，divide and conquer）
## D&C工作原理（同递归，二者是相同的）：
# （1）找出收敛条件
# （2）确定如何缩小问题规模，最终符合收敛条件
# note：D&C不是一个具体的算法，但是是一种解决问题的思路

## eg1：求数组中的元素和（若空数组则返回0）
## 方法1：直接循环
## 方法2：利用D&C
total=0
def sum(arr,total):
    if(len(arr)==0): ## 收敛条件
        return total
    else: ## 递归条件
        total=total+arr.pop(0)
        return sum(arr,total)

arr=[1,3,5,6,8]
print(sum(arr,total))

## eg2：二分查找的递归实现
def binary_search(arr, target):
    if(len(arr)==0):
        return "no"
    elif(len(arr)==1 and arr[0]==target):
        return "yes"
    elif(len(arr)==1 and arr[0]!=target):
        return "no"
    else:
        left=0
        right=len(arr)-1
        mid=(left+right)//2

        if(arr[mid]>target):
            return binary_search(arr[left:(mid-1)],target)
        elif(arr[mid]<target):
            return binary_search(arr[mid+1:right],target)
        else:
            return "yes"
arr=[1,3,5,6,8,9,12]
target=8
print(binary_search(arr,target))