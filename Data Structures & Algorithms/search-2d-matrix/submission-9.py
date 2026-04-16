class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l,r = 0 , len(matrix[0])-1
        u,d = 0, len(matrix) - 1
        while u <= d:
            mid_row = (u+d)//2
            if target < matrix[mid_row][0]:
                d = mid_row - 1
            elif target > matrix[mid_row][-1]:
                u = mid_row + 1
            else:
                break
        if u > d:
            return False
        while l <= r:
            mid_col = (l+r)//2
            if target == matrix[mid_row][mid_col]:
                return True
            elif target < matrix[mid_row][mid_col]:
                r = mid_col -1
            else:
                l = mid_col + 1
        return False