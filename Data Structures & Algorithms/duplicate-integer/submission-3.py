class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if n in count and count[n]==1:
                return True
            count[n] = 1            
        return False

