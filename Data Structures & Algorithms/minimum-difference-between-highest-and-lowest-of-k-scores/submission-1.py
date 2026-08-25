class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        min_value = float("inf")
        for i in range(len(sorted_nums)-k+1):
            k_nums = sorted_nums[i:i+k]
            print(k_nums)
            min_value_k = k_nums[-1] - k_nums[0]

            min_value = min(min_value, min_value_k)

        return min_value
