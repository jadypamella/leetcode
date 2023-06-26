# URL: https://leetcode.com/problems/can-place-flowers
# Time complexity: O(n)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # initializing variables
        length = len(flowerbed)
        count = 0
        i = 0

        # if there are no empty plot
        if n == 0:
            return False

        # for each plot in the array flowerbed
        while i < length:

            # if a plot is empty (0) and adjacent plots are also empty, then we can plant a flower on it
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True

            # next plot        
            i += 1

        return False
