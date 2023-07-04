# URL: https://leetcode.com/problems/move-zeroes/
# Time complexity: O(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # initialize two pointers, one to go through the list and one to track the position of zeros
        left = 0
        zero_pos = 0
    
        # loop through the list
        while left < len(nums):
        
            # if the current element is non-zero, move it to the zeros position
            if nums[left] != 0:
                nums[zero_pos] = nums[left]
                zero_pos += 1
        
            left += 1
    
        # fill the rest of the list with zeros
        while zero_pos < len(nums):
            nums[zero_pos] = 0
            zero_pos += 1
        
        return nums
