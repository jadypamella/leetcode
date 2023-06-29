# URL: https://leetcode.com/problems/reverse-words-in-a-string/
# Time complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        
        # split the string into a list of words
        words = s.split()
        
        # reverse the order of the word list       
        words.reverse()

        # join the words into a string, separated by a single space
        return ' '.join(words)
