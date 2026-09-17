class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if len(stack)>0 and s[stack[-1]] =="(":
                    stack.pop()
                else:
                    stack.append(i)
        
        res = [c for c in s]
        for i in stack[::-1]:
            res.pop(i)
        return "".join(res)
