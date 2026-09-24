class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = []

        for i in range(len(s)):
            res.append([s[i], 0])
            if len(res) == 1 or res[-1][0] != res[-2][0]:
                res[-1][1] = 1

            else:
                res[-1][1] = res[-2][1] + 1

            if res[-1][1] == k:
                for _ in range(k):
                    res.pop()


        res = "".join([t[0] for t in res])
        return res





            

        
       


