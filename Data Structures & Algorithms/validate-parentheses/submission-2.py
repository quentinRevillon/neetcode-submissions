class Solution:
    def isValid(self, s: str) -> bool:


        p = []
        for c in s:
            if c == "(" or c=="{" or c=="[":
                p.append(c)
            elif len(p)==0 and (c==")" or c=="}" or c=="]"):

                return False
            elif c==")":
                if p[-1]=="(":
                    p.pop()
                else:
                    return False
            elif c=="}":
                if p[-1]=="{":
                    p.pop()
                else:
                    return False
            elif c=="]":
                if p[-1]=="[":
                    p.pop()
                else:
                    return False

        return len(p)==0
