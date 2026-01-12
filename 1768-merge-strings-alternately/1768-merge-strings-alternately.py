class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        len_w1, len_w2 = len(word1), len(word2)
        min_len = min(len_w1, len_w2)

        for i in range(min_len):
            output += word1[i] + word2[i]
        
        if len_w1 > len_w2:
            output += word1[min_len:]
        else:
            output += word2[min_len:]
        
        return output