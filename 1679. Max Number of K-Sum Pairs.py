# URL: https://leetcode.com/problems/max-number-of-k-sum-pairs
# Time complexity: O(n)

class Solution:
     def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {} # hash table (dictionary) to store the frequency of each number
        count = 0 # operation counter

        for num in nums: # iterates over each number in the array
            complement = k - num # calculate the complement of the current number
            if complement in freq and freq[complement] > 0: # check if the complement exists in the hash table and if it has a frequency greater than 0
                count += 1 # increment the operations counter
                freq[complement] -= 1 # decrement the complement frequency in the hash table
            else:
                freq[num] = freq.get(num, 0) + 1 # update the frequency of the current number in the hash table

        return count # returns the maximum number of operations
