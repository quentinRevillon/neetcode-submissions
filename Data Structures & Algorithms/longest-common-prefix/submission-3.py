class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i, l in enumerate(strs[0]):
          
            for j, w in enumerate(strs):
                if len(w)<=i:
                    return prefix
                if strs[j][i] != strs[0][i]:
                    return prefix
            
            prefix += strs[0][i]
        return prefix