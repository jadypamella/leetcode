# URL: https://leetcode.com/problems/greatest-common-divisor-of-strings
# Time complexity: O(N*M*N), where N is the length of the longest string between str1 and str2 and M is the length of str2.

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        
        # make sure that str1 is always the longest string
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        # return str1 if they are equal
        if str1 == str2:
            return str1

        gcd_str = ""

        # exhaustive search
        for i in range(1, len(str2) + 1):
            if len(str2) % i == 0:
                substr = str2[:i]
                if str1.replace(substr, "") == "" and str2.replace(substr, "") == "":
                    gcd_str = substr

        return gcd_str
