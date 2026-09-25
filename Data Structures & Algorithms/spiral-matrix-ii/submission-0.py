class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        import numpy as np
        mat = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        vect = [0, 1]
        c = 1
        while c <= n**2:
            print(i, j)
            mat[i][j] = c
            c+=1
            
            if i + vect[0]>= n or i + vect[0]< 0 or j+vect[1] >= n or j+vect[1] < 0 or mat[i+vect[0]][j+vect[1]] > 0:
                vect = np.dot(np.array([[0, 1],[-1, 0]]), np.array(vect))
            
            i += vect[0]
            j += vect[1]

        return mat
        