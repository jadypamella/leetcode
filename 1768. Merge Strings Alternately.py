# URL: https://leetcode.com/problems/merge-strings-alternately
# Time complexity: O(n)

class Solution(object):
    def mergeAlternately(self, word1, word2):

        # result string
        merged = ""

        # counters for each word
        i, j = 0
        
        # loop until i is less than the length of word1
        for i in range(len(word1)):

            # include the character value of word1
            merged += word1[i]
            
            if j < len(word2):

                # include the character value of word2
                merged += word2[j]
                j += 1
        
        # if there are still characters in word2, add them in the result
        merged += word2[j:]
        
        return merged
