# URL: https://leetcode.com/problems/increasing-triplet-subsequence/
# Time complexity: O(n)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # defining the variables as a infinite float
        first = float('inf')
        second = float('inf')

        # looking for the triplets
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
