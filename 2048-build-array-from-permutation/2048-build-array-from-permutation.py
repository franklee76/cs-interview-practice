class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        lists = []
        for x in range(len(nums)):
            lists.append(nums[nums[x]])
        return lists