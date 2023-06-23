# URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
# Time complexity: O(n)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        result = []

        # getting the original max value of candies
        max_candies = max(candies)
        
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
