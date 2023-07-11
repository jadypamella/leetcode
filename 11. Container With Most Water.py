# URL: https://leetcode.com/problems/container-with-most-water
# Time complexity: O(n)

class Solution:
    def maxArea(self, height: List[int]) -> int:
    
        # defining the max area and two pointers
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:

            # calculate the current area
            h = min(height[left], height[right])
            w = right - left
            area = h * w

            # update the maximum area
            max_area = max(max_area, area)
            
            # move the pointer left or right according to the height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
