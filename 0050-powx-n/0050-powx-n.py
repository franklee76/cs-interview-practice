class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calcPow(x, n):
            if n == 0:
                return 1
            elif n < 0:
                return calcPow (1/x, -n)
            else:
                divide = calcPow(x, n//2)
                output = divide * divide
                if n % 2 == 1:
                    output *= x
                return output
        
        return calcPow(x, n)
            
