class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, col, i):
            #Base case
            if i == len(word): return True

            if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[i]):
                return False

            letter = board[row][col]
            board[row][col] = '_'   #So we dont reuse this cell

            ans = dfs(row-1, col, i+1) or dfs(row+1, col, i+1) or dfs(row, col-1, i+1) or dfs(row, col+1, i+1)
            board[row][col] = letter    #Put letter back for next attempts
            return ans

            

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]: #Start DFS
                    if dfs(row, col, 0): return True


        return False