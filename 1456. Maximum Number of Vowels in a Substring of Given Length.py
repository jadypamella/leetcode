# URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
# Time complexity: O(n)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowel_count = 0
        vowel_count = 0

        # count vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        max_vowel_count = vowel_count

        # move the sliding window and update vowel count
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                vowel_count -= 1
            if s[i] in vowels:
                vowel_count += 1
            max_vowel_count = max(max_vowel_count, vowel_count)

        return max_vowel_count
