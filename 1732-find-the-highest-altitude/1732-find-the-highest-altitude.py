class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi, current = 0, 0
        for i in range(len(gain)):
            current += gain[i]
            if current > maxi:
                maxi = current
        return maxi