class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        freq = [Counter(w) for w in words]
        min_f = freq[0]
        for c in min_f:
            for f in freq:
                min_f[c] = min(min_f[c], f[c])

        r = []
        for c, f in min_f.items():
            for i in range(f):
                r.append(c)
        
        return r
