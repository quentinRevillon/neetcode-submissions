from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k, v in c.items():
            if v > int(len(nums)/2):
                return k
        