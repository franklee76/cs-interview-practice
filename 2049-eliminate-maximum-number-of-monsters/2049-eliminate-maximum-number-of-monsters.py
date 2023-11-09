class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        count = 0
        time = []
        for x in range(len(speed)):
            time.append(ceil(dist[x]/speed[x]))
        
        time = sorted(time)
        for y in range(len(time)):
            if y >= time[y]: break
            count += 1
        
        return count

        