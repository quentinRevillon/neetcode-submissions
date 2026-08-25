class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, k-1
        diff = float('inf')
        while j!=len(nums):
            diff = min(diff, nums[j]-nums[i])
            i+=1
            j+=1
        return diff


