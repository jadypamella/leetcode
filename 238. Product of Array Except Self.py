# URL: https://leetcode.com/problems/product-of-array-except-self/
# Time complexity: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Initialize results in the size of nums
        n = len(nums)
        answer = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        # Define the first value of prefix and the last value of suffix equals to 1
        prefix[0] = 1
        suffix[n - 1] = 1
        
        # Calculate prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # Calculate answer
        for i in range(n):
            answer[i] = prefix[i] * suffix[i]
        
        return answer
