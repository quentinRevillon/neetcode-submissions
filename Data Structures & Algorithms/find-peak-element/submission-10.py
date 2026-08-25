class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        l, r = 1, len(nums)-2
        
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid-1]>nums[mid]:
                r = mid-1
            elif nums[mid+1]>nums[mid]:
                l = mid+1
            else:
                return mid-1