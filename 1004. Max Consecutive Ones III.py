# URL: https://leetcode.com/problems/max-consecutive-ones-iii/
# Time complexity: O(n)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left, right = 0, 0  # pointers to track the sliding window
        max_ones = 0        # maximum number of consecutive 1's seen so far
        zero_count = 0      # number of zeros encountered in the current window

        while right < len(nums):  # iterate through the array using 'right' pointer
            if nums[right] == 0:
                zero_count += 1   # increment 'zero_count' if the current element is 0

            while zero_count > k:  # if the number of zeros exceeds 'k', adjust the window's left boundary
                if nums[left] == 0:
                    zero_count -= 1  # decrement 'zero_count' if the element at 'left' was 0
                left += 1            # move the left pointer to the right

            # update 'max_ones' with the maximum of the current size of consecutive 1's or the previous maximum
            max_ones = max(max_ones, right - left + 1)
            right += 1  # move the right pointer to the right

        return max_ones
