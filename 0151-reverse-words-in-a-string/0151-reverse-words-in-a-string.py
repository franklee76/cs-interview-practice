class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        reverse = [word.pop() for i in range(len(word))]
        return " ".join(reverse)