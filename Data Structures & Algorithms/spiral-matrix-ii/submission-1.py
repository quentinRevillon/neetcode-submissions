class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(0, n)] for _ in range(n)]
        vect = [0, 1]
        i, j = 0, -1
        c = 0
        while c < n**2:
            k, l = i + vect[0], j + vect[1]
            print(k,l)
            if k < 0 or l < 0 or k >= n or l >= n or res[k][l] > 0:
                vect = [vect[1], -vect[0]]
            i, j = i + vect[0], j + vect[1]
            c+=1
            res[i][j] = c
        return res
            


        