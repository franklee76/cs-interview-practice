class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        count = 0
        for x in nums:
            heapq.heappush(max_heap, -x)
        while k-1 > count:
            heapq.heappop(max_heap)
            count+=1
        return -heapq.heappop(max_heap)