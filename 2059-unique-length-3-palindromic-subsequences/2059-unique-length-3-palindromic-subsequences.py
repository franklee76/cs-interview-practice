class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = set(s)
        ans = 0
        for char in chars:
            first, last = s.find(char), s.rfind(char)
            ans += len(set(s[first+1:last]))
        return ans
