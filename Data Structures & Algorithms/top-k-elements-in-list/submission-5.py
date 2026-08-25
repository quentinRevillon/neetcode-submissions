class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n]+=1

        count_groups = defaultdict(list)
        for n in nums:
            if n not in count_groups[count[n]]:
                count_groups[count[n]].append(n)
        
        print(count)
        print(count_groups)

        max_freq = max(count_groups.keys())
        mf_elts = []

        for freq in range(max_freq, 0, -1):
            mf_elts += count_groups[freq]
            if len(mf_elts)>=k:
                break
        return mf_elts


