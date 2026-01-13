class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        products = [1] * numsLen
        for x in range (1, numsLen):
            products[x] = products[x-1] * nums[x-1]
        
        right= nums[-1]
        for y in range (numsLen-2, -1, -1):
            products[y] *= right
            right *= nums[y]
        
        return products