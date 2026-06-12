class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        queue = deque()
        minutes = 0
        fresh = 0

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    queue.append((x, y))
                    visited.add((x, y))
                elif grid[x][y] == 1:
                    fresh += 1

        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy 
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 1:
                        fresh -= 1
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        
        return minutes if fresh == 0 else -1