class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxi, count = 0, 0
        vowel = {'a','e', 'i','o','u'}

        for i in range(len(s)):
            if s[i] in vowel:
                count += 1
            if i >= k - 1:
                maxi = max(maxi, count)
                if s[i - k + 1] in vowel:
                    count -= 1

        return maxi