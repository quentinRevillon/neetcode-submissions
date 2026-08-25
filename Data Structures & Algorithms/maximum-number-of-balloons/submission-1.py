class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        res=0

        while cnt["b"]>0 and cnt["a"]>0 and cnt["l"]>1 and cnt["o"]>1 and cnt["n"]>0:
            cnt["b"]-=1
            cnt["a"]-=1
            cnt["l"]-=2
            cnt["o"]-=2
            cnt["n"]-=1
            res+=1
        return res
        