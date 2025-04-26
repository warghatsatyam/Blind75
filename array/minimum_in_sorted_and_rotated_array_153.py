from typing import List
def findMin(nums: List[int]) -> int:
    """
    Find the minimum element in a rotated sorted array.
    
    :param nums: List[int] - A rotated sorted array
    :return: int - The minimum element in the array
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if mid is greater than the rightmost element
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
            
    return nums[left]

# Example usage
if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    print(findMin(nums))  # Output: 1
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(findMin(nums))  # Output: 0
    nums = [1]
    print(findMin(nums))  # Output: 1
    nums = [2, 1]
    print(findMin(nums))  # Output: 1