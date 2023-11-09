class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        count = 0
        row, col = len(maze), len(maze[0])
        x, y = entrance[0], entrance[1]
        queue = deque([(entrance[0], entrance[1])]) #position to visit
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue: #until position to visit not empty
            for n in range(len(queue)):
                i, j = queue.popleft() #pop the leftmost

                if count > 0 and (i, j) != (x, y) and (i == 0 or i == row - 1 or j == 0 or j == col - 1): #boundary condition
                    return count
                
                for dx, dy in move:
                    i1, j1 = i + dx, j + dy
                    if 0 <= i1 < row and 0 <= j1 < col and maze[i1][j1] == '.' :
                        queue.append((i1, j1))
                        maze[i1][j1] = '+'
            
            count += 1

        return -1


