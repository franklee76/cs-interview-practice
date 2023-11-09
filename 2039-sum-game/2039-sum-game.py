class Solution:
    def sumGame(self, num: str) -> bool:
        LH, RH = list(num[:int(len(num)/2)]), list(num[int(len(num)/2):])
        sumLH = sumRH = questLH = questRH = 0
        for x,y in zip(LH, RH):
            if x == '?': questLH +=1
            else: sumLH += int(x)
            if y == '?': questRH +=1
            else: sumRH += int(y)
        
        return not (2*sumLH + 9*questLH == 2*sumRH + 9*questRH)
