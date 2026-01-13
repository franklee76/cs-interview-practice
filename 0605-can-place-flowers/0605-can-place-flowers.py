class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed_len = len(flowerbed)

        for i in range(bed_len):
            if n <= 0:
                break
            prev = i == 0 or flowerbed[i-1] == 0
            nex = i == bed_len - 1 or flowerbed[i+1] == 0
            if prev and nex and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0