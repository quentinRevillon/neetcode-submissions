class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_people_cnt={}
        trusting_people_cnt={}

        for t in trust:
            trusted_people_cnt[t[1]] = trusted_people_cnt.get(t[1], 0) + 1
            trusting_people_cnt[t[0]] = trusting_people_cnt.get(t[0], 0) + 1

        for key, val in trusted_people_cnt.items():
            if val==n-1 and not key in trusting_people_cnt.keys():
                return key

        return -1



        