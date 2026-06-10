class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        def search(x, y, idx):
            if board[x][y] != word[idx]:
                return False
            
            if idx == len(word) - 1:
                return True 
            
            visited.add((x, y))

            for dx, dy in directions: 
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    if search(nx, ny, idx + 1):
                        return True 
            
            visited.remove((x, y))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if search(r, c, 0):
                        return True 
        
        return False