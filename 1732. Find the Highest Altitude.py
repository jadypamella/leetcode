# URL: https://leetcode.com/problems/find-the-highest-altitude
# Time complexity: O(n)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

         # initialize variables to keep track of the maximum altitude and current altitude
        max_altitude = 0
        current_altitude = 0
        
        # loop through the 'gain' array to calculate the altitude at each point of the road trip
        for g in gain:
            
            # update the current altitude by adding the gain at the current point
            current_altitude += g
            
            # update the maximum altitude seen so far if the current altitude is higher
            max_altitude = max(max_altitude, current_altitude)
        
        # return the highest altitude encountered during the road trip
        return max_altitude
