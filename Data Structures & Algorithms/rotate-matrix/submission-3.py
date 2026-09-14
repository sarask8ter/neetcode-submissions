class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topLeft = matrix[top][l+i]
                # top row
                matrix[top][l+i] = matrix[bottom-i][l]
                # left row
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # bottom row
                matrix[bottom][r-i] = matrix[top+i][r]
                # right row
                matrix[top+i][r] = topLeft
        
            r -= 1
            l += 1
