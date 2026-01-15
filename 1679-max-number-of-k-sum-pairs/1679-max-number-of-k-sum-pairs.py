class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j, count = 0, len(nums)- 1, 0
        while i < j:
            sums = nums[i] + nums[j]
            if sums == k:
                count += 1
                i += 1
                j -= 1
            elif sums > k:
                j -= 1
            else:
                i += 1
        return count