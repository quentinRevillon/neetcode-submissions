class Solution:
    def findPeakElement(self, nums: List[int]) -> int:


        
        nums = [float('-inf')] + nums + [float('-inf')]
        i = 1
        j = len(nums)-2

        # while True:
        if nums[i]>nums[i+1]:
            return i - 1
        elif nums[j]>nums[j-1]:
            return j - 1

        mid = (i+j)//2
           
        while nums[mid-1]>=nums[mid] or nums[mid+1]>=nums[mid]:

            if nums[mid-1]>nums[mid]:
                j = mid
            elif nums[mid+1]>nums[mid]:
                i = mid
            mid = (i+j)//2

        return mid -1


