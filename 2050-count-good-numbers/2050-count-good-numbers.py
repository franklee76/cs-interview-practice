class Solution:
    def countGoodNumbers(self, n: int) -> int:
        comb = pow(20, floor(n/2), 1000000007)
        if n % 2 == 1: comb *= 5
        
        return comb % 1000000007
            

