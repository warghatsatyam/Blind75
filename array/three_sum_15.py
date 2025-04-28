from typing import List

def three_sum(nums: List[int], target: int) -> List[List[int]]:
    final_three_sum_pairs = []
    nums.sort()

    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:  # safe check for i > 0
            two_sum_target = target - nums[i]
            three_sum_pairs = two_sum(nums[i+1:], two_sum_target, nums[i])
            if three_sum_pairs:
                final_three_sum_pairs.extend(three_sum_pairs)  # extend instead of append
    
    return final_three_sum_pairs

def two_sum(nums: List[int], target: int, append_value: int) -> List[List[int]]:
    hashmap = {}
    two_sum_pairs = []

    for num in nums:
        diff = target - num
        if diff in hashmap:
            pair = sorted([append_value, num, diff])
            if pair not in two_sum_pairs:  # avoid duplicates
                two_sum_pairs.append(pair)
        else:
            hashmap[num] = 1

    return two_sum_pairs if two_sum_pairs else None

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    arr = three_sum(nums=nums, target=0)
    print(arr)
