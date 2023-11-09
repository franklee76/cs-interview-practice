class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        count = prev = 0
        for r in rungs:
            count += (r - prev - 1) // dist
            prev = r
        return count