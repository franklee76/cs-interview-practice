class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        max = sums
        for x in range(k, len(nums)):
            sums += nums[x] - nums[x - k]
            if max < sums:
                max = sums
        return max / float(k)
