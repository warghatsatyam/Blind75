from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        hash_map = {}
        i=0
        for num in nums:
            diff = target-num
            if diff in hash_map:
                return [hash_map[diff],i]
            else:
                hash_map[num]=i
                i = i+1
        return []


if __name__ == '__main__':
    nums = [2,7,11,5]
    target = 9
    ans = twoSum(nums=nums,target=target)
    print(ans)