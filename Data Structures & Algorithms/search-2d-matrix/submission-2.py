class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # for i in matrix:w
        l, r = 0, (len(matrix) * len(matrix[0])) -1
        #     if i[r] < target:
        #         continue
        #     else:
        while l<=r:
            mid = l + ((r-l) // 2)
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

        