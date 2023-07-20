# URL: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
# Time complexity: O(n)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_length = 0   # initialize the maximum length of the subarray with only 1's (after deletion) to 0
        left = 0         # initialize the left pointer of the sliding window to 0
        zero_count = 0   # initialize the count of zeros in the current window to 0

        for right in range(len(nums)):   # iterate through the array using the right pointer
            if nums[right] == 0:         # if the current element is 0, increment the zero_count
                zero_count += 1

            while zero_count > 1:        # if there are more than one zeros in the window, we need to update the window
                if nums[left] == 0:      # if the left element is 0, decrement the zero_count
                    zero_count -= 1
                left += 1                # increment the left pointer to slide the window to the right

            max_length = max(max_length, right - left)   # update the max_length with the current window size

        return max_length   # return the maximum length of the subarray with only 1's (after deletion)
