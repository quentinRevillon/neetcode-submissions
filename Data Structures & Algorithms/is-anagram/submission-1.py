class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        words = [s, t] 

        words_letters = [{}, {}]
        
        for wi in range(2):
            w = words[wi]
            letters = words_letters[wi]
            for l in w:
                if l in letters:
                    letters[l] +=1
                else:
                    letters[l] = 1

        all_keys = list(words_letters[0].keys()) + list(words_letters[1].keys())
        print(words_letters[0], words_letters[1])
        for k in all_keys:
            if k not in words_letters[0] or k not in words_letters[1] or words_letters[0][k] != words_letters[1][k]:
                return False
            
        return True
            
        

        