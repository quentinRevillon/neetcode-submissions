class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = defaultdict(int)
        voyels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(len(words)):
            if (len(words[i])==1 and words[i] in voyels) or (words[i][0] in voyels and words[i][-1] in voyels):
                prefix_sum[i] = prefix_sum[i-1] + 1
            else:
                prefix_sum[i] = prefix_sum[i-1]
        print(prefix_sum)
        ans = []
        for query in queries:
            li, ri = query
            ans.append(prefix_sum[ri]-prefix_sum[li-1])
        return ans

