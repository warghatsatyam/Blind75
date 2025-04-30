from typing import List
# 15. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with the x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.
# The container with the most water is the one that has the maximum area. The area of a container is defined as the minimum of the two heights multiplied by the distance between them.
# The two lines are represented by their heights in the array. The area is calculated as min(height[i], height[j]) * (j - i).
# The brute force solution is to check all pairs of lines, which takes O(n^2) time. A more efficient solution is to use a two-pointer approach, which takes O(n) time.
# The two-pointer approach works by initializing two pointers at the beginning and end of the array. The area is calculated using the heights at the two pointers, and the pointer with the smaller height is moved towards the other pointer. This process is repeated until the two pointers meet.
# The time complexity of the two-pointer approach is O(n) and the space complexity is O(1).

def maxArea(height: List[int]) -> int:
    max_area = 0
    l = 0
    r = len(height)-1
    while l<r:
        h = min(height[l],height[r])
        w = r-l
        current_area = h*w 
        if current_area > max_area:
            max_area = current_area
        
        if height[l] > height[r]:
            r = r-1
        else:
            l = l+1 

    return max_area 


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    area = maxArea(height=height)
    print(area)