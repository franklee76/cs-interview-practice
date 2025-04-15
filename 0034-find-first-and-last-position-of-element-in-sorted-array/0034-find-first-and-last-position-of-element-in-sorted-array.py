class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(target: int) -> int:
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        left = find(target)
        right = find(target + 1) - 1

        if left <= right:
            return [left, right]

        return [-1, -1]