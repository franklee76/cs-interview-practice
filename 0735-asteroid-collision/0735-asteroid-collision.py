class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        
        for i in asteroids:
            while res and i < 0 < res[-1]:
                if abs(i) > abs(res[-1]):
                    res.pop()
                    continue
                elif abs(i) == abs(res[-1]):
                    res.pop()
                break
            else:
                res.append(i)
        return res

            
                
                