class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = duration
        for x in range (len(timeSeries)-1):
            count += min(duration, timeSeries[x+1]-timeSeries[x])
        return count
        