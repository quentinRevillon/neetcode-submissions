class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i,j,k = 0,1,2
        if len(nums) == 1:
            return 0
        while (k != len(nums)):
            if nums[j]>nums[i] and nums[j]>nums[k]:
                return j
            j +=1
            i +=1
            k+=1
        

        if nums[0]> nums[-1]:
            return 0
        else: 
            return len(nums)-1