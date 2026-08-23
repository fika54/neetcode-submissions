class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) - 1
        middle = 0

        while l <= r:
            middle = (l + r) // 2
            check = matrix[middle][0]

            if check == target:
                return True
            elif check < target:
                l = middle + 1
            else:
                r = middle - 1

        if matrix[middle][0] > target:
            middle -= 1
        
        if middle < 0:
            return False


        l = 0
        r = len(matrix[middle]) - 1

        while l <= r:
            m = (l + r) // 2
            check = matrix[middle][m]
            if check == target:
                return True
            elif check < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
