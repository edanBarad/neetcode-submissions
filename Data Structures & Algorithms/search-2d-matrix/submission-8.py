class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        bottom, top = 0,  len(matrix)-1

        while bottom <= top:
            middle = (bottom + top) // 2
            if matrix[middle][-1] == target:
                return True
            elif matrix[middle][-1] < target:
                bottom = middle + 1
            else:
                top = middle -1

        row = bottom
        if target < matrix[row][0]:
            return False
            
        print("Row is ", row)
        left, right = 0, len(matrix[0])-1
        
        while left <= right:
            middle = (left+right)//2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False