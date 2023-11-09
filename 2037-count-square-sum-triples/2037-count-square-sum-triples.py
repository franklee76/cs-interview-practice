class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        square = {x * x for x in range(2, n+1)}
        for a, b in combinations(square, 2):
            if a + b in square: count += 2
        return count
        