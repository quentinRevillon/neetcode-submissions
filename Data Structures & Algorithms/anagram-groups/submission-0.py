class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s: str, t: str):
            if len(s) != len(t):
                return False
            
            countS, countT = {}, {}
            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)

            return countS == countT

        # def isAnagram(s: str, t: str):
        #     return sorted(s) == sorted(t) 

        anagram_groups = []
        while len(strs) > 0:
            ref = strs[0]
            anagram_groups.append([ref])
            new_strs = []

            for i in range(1, len(strs)):
                s = strs[i]
                if isAnagram(ref, s):
                   anagram_groups[-1].append(s)
                else:
                    new_strs.append(s)

            strs = new_strs    

        return anagram_groups 
            
