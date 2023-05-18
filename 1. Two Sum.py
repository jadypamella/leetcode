# URL: https://leetcode.com/problems/two-sum/
# Time complexity: O(n2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # The size of the list
        n = len(nums)

        for i in range(n):

            # Starting the iteration from the next element after the current element (nums[i])
            for j in range(i + 1, n):

                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # No solution found
        return []
