from typing import List


#Approach1
def containsDuplicateApproach1(nums: List[int]) -> bool:
    processed_nums = set()
    for num in nums:
        if num in processed_nums:
            return True
        else:
            processed_nums.add(num)
    return False

#Approach2
def containsDuplicateApproach2(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

#Approach3 
def containsDuplicateApproach3(nums: List[int]) -> bool:
    processed_nums = {}
    for num in nums:
        if num in processed_nums:
            return True
        else:
            processed_nums[num] = 1
    return False

nums = [1,2,3,1]
if __name__ == '__main__':
    print(containsDuplicateApproach1(nums))
    print(containsDuplicateApproach2(nums))
    print(containsDuplicateApproach3(nums))
    
