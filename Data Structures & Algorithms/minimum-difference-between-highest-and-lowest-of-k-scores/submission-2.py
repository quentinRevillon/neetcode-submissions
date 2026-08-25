class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sort_nums = sorted(nums)
        i, j = 0, k-1
        res = float('inf')
        while j != len(nums):
            res = min(res, sort_nums[j]-sort_nums[i])
            i+=1
            j+=1

        return res
