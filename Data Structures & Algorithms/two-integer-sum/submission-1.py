class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        ids_divided_target = []

        for i, n in enumerate(nums):
            if n != target/2:
                nums_dict[n] = i
            else:
                ids_divided_target.append(i)

        if len(ids_divided_target)==2:
            return sorted(ids_divided_target)
        else:
            for k in nums_dict.keys():
                if target-k in nums_dict:
                    return sorted([nums_dict[k], nums_dict[target-k]])
            