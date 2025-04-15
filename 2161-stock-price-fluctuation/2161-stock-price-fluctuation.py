import heapq

class StockPrice:

    def __init__(self):
        """Set empty data structures"""
        self.price_map = {}
        self.latest_timestamp = 0
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        """Update on price list, min/max heap and latest timestamp"""
        self.price_map[timestamp] = price
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))
        if timestamp > self.latest_timestamp: self.latest_timestamp = timestamp

    def current(self) -> int:
        """"Return price for latest timestamp"""
        return self.price_map[self.latest_timestamp]

    def maximum(self) -> int:
        """Return maximum price"""
        while self.max_heap and self.price_map[self.max_heap[0][1]] != -self.max_heap[0][0]:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]
        

    def minimum(self) -> int:
        """Return minimum price"""
        while self.min_heap and self.price_map[self.min_heap[0][1]] != self.min_heap[0][0]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()