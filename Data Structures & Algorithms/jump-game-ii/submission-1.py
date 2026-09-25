class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = defaultdict(int)

        def rec(i: int) -> int:

            if i == len(nums) - 1:
                return 0
        

            minimal = math.inf
            for j in range(i+1, min(i+1+nums[i], len(nums))):
                if j in memo:
                    next_minimal = memo[j]
                else:
                    next_minimal = rec(j)
                    memo[j] = next_minimal
                minimal = min(minimal, next_minimal)


            return minimal + 1


        return rec(0)

        