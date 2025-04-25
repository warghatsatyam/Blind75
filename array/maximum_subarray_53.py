from typing import List

def maximum_subarray(nums:List[int])-> int:
    curr_sum = max_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(num,curr_sum+num)
        max_sum = max(max_sum,curr_sum)
    return max_sum


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum = maximum_subarray(nums)
    print(max_sum)