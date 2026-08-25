class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1, l2 = [], []

        for n in nums1:
            if not n in l1 and not n in nums2:
                l1.append(n)

        for n in nums2:
            if not n in l2 and not n in nums1:
                l2.append(n)


        return [l1, l2]