class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
            
        left, right = 0, (len(matrix)*len(matrix[0]))-1
        while left <= right:
            middle = (left + right) // 2
            val = matrix[middle//len(matrix[0])][middle%len(matrix[0])]
            if val == target:
                return True;
            elif val < target:
                left = middle + 1
            else:
                right = middle - 1
        return False