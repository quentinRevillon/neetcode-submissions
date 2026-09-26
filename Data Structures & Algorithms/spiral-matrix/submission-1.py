class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        vect = [0, 1]
        i, j = 0, 0
        c = 0
        while c < len(matrix)*len(matrix[0]):
            res.append(matrix[i][j])
            matrix[i][j] = "done"
            next_i, next_j = i+vect[0], j+vect[1]
            # print(next_i, next_j)
            # print(matrix[next_i][next_j])
            if next_i >= len(matrix) or next_j >= len(matrix[0]) or matrix[next_i][next_j] == "done":
                vect = [vect[1], -vect[0]]
                next_i, next_j = i+vect[0], j+vect[1]

            i, j = next_i, next_j
            c+=1  
        return res          