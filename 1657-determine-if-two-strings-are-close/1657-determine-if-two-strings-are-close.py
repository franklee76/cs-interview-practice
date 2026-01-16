class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        dict1, dict2 = {}, {}

        for x in range(len(word1)):
            if word1[x] in dict1:
                dict1[word1[x]] += 1
            else:
                dict1[word1[x]] = 1

            if word2[x] in dict2:
                dict2[word2[x]] += 1
            else:
                dict2[word2[x]] = 1
        
        if set(dict1.keys()) == set(dict2.keys()) and sorted(dict1.values()) == sorted(dict2.values()):
            return True
        return False
