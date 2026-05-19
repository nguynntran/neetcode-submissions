class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p_idx = 0
        for i in range(len(matrix) - 1):
            if matrix[i][0] == target or matrix[i + 1][0] == target:
                return True
            elif (matrix[i][0] < target < matrix[i + 1][0]):
                p_idx = i
            elif target > matrix[i + 1][0]:
                p_idx = i + 1
        l, r = 0, len(matrix[p_idx]) - 1
        while l <= r:
            mid = (r + l) // 2
            if matrix[p_idx][mid] == target:
                return True
            if matrix[p_idx][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False