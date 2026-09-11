class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        sorted_nums_inc = sorted(nums)
        sorted_nums_dec = sorted(nums, key=lambda x:-x)
        if sorted_nums_inc == nums or sorted_nums_dec == nums:
            return True
        else:
            return False