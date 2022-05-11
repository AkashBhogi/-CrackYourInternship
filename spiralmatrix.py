class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [];r= len(matrix);c=len(matrix[0]);row_start,col_start=0,0
        row_end, col_end = r-1,c-1
        while len(res) < (r*c):
            temp_col_start=col_start
            temp_row_start = row_start
            while col_start <= col_end and len(res) < (r*c):
                res.append(matrix[row_start][col_start])
                col_start += 1
            col_start -= 1
            row_start += 1
            while row_start <= row_end and len(res)<(r*c):
                res.append(matrix[row_start][col_start])
                row_start += 1
            col_start -= 1
            row_start -= 1
            while col_start > temp_col_start and len(res) < (r*c):
                res.append(matrix[row_start][col_start])
                col_start -= 1
            while row_start > temp_row_start and len(res) <(r*c):
                res.append(matrix[row_start][col_start])
                row_start -= 1
            row_start += 1
            col_start += 1
            row_end -= 1
            col_end -= 1

        return res
