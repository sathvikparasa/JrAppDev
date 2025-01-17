class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Using a bool to check whether the first row is zero or not
        first_row_zero = False

        # Loop through matrix and find all 0s
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    # Skip the first row, but if there is, then store it in the bool
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        first_row_zero = True
        
        # Skip the first row/col and change all the other rows/cols to 0
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[r])):
                if (matrix[r][0] == 0 or matrix[0][c] == 0):
                    matrix[r][c] = 0
        
        # Change the first column to zero
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        # Change the first row to zero
        if first_row_zero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0