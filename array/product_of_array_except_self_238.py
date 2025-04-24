from typing import List


# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The problem can be solved in O(n) time and O(1) space complexity.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Approach 1:
def productExceptSelfApproach1(nums: List[int]) -> List[int]:
    prefix = [1 for x in range(len(nums))]
    postfix = [1 for x in range(len(nums))]
    ans = [1 for x in range(len(nums))]
    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1] * nums[i-1]
    for i in range(len(nums)-2, -1,-1):
        postfix[i] = postfix[i+1] * nums[i+1]
    for i in range(len(nums)):
        ans[i] = prefix[i] * postfix[i]
    return ans


# Approach 2:
# The above approach can be optimized to O(1) space complexity by using the output array to store the prefix product and then updating it with the postfix product.
def productExceptSelfApproach2(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1] * n
    prefix = 1
    postfix = 1
    for i in range(1,n):
        ans[i] = nums[i-1] * prefix
        prefix = ans[i]
    for j in range(n-2, -1, -1):
        postfix = nums[j+1] * postfix
        ans[j] *= postfix
    return ans
if __name__ == '__main__':
    nums = [1,2,3,4]
    print(productExceptSelfApproach1(nums))
    print(productExceptSelfApproach2(nums))