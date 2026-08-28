class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        firstOc = {}
        lastOc = {}
        r=set()

        for i, c in enumerate(s):
            if not c in firstOc.keys():
                firstOc[c] = i
            lastOc[c] = i
        print("firstOc", firstOc)
        print("lastOc", lastOc)
        for code in range(ord("a"), ord("z")+1):
            c = chr(code)
            fOc = firstOc.get(c, False)
            lOc = lastOc.get(c, False)
            print("c", c)
            print("fOc", fOc)
            print("lOC", lOc)
            if c in firstOc.keys() and c in lastOc.keys():
                for l in s[fOc+1:lOc]:
                    r.add(c+l+c)
            
        return len(r)