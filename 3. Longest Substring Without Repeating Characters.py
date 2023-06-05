# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time complexity: O(n)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # variables to track the sliding window
        left = 0 # left index of the window
        right = 0 # right index of the window
        max_length = 0 # max substring length
        seen_chars = set() # set of unique characters in the current substring

        while right < len(s):
            if s[right] not in seen_chars:
                # if the character is not in the current substring, add it to the set and expand the window
                seen_chars.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                # if the character is already in the current substring, remove the leftmost character and shrink the window
                seen_chars.remove(s[left])
                left += 1

        return max_length
