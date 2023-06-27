# URL: https://leetcode.com/problems/reverse-vowels-of-a-string
# Time complexity: O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:

        # all vowels considered
        vowels = set('aeiouAEIOU')
        
        # transform string into a list
        s = list(s)

        # initializing pointers
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] in vowels:
                j -= 1
            elif s[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1

        # joins all elements of list s into a string
        return ''.join(s)
