class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        result = [False] * len(candies)

        for x in range(len(candies)):
            if candies[x] > max:
                max = candies[x]
        
        for x in range(len(candies)):
            if candies[x] + extraCandies >= max:
                result[x] = True

        return result