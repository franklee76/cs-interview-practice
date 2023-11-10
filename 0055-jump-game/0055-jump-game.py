class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i > reach: return False
            if reach < i + nums[i]: reach = i + nums[i]
        return True