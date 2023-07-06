# URL: https://leetcode.com/problems/is-subsequence
# Time complexity: O(n)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        j = 0

        # iterate while there are characters to process in both 's' and 't'
        while (i < len(s)) and (j < len(t)):

            # If the characters at positions 'i' and 'j' are equal
            if (s[i] == t[j]):
                i += 1  # move to the next character in 's'
            
            j += 1  # move to the next character in 't'

        # check if all characters in 's' have been found in 't' in order
        if (i == len(s)):
            return True
            
        return False
