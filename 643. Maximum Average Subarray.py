# URL: https://leetcode.com/problems/maximum-average-subarray-i
# Time complexity: O(n)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)  # length of the array nums
        window_sum = sum(nums[:k])  # sum of the first k elements
        max_sum = window_sum  # initialize the maximum sum as the sum of the first k elements

        # iterate from k to n - 1 (inclusive)
        for i in range(k, n):
            
            # update the window sum by subtracting the element going out and adding the element coming in
            window_sum = window_sum - nums[i - k] + nums[i]
            
            # update the maximum sum if the current window sum is greater
            max_sum = max(max_sum, window_sum)

        # return the maximum average by dividing the maximum sum by k
        return max_sum / k
