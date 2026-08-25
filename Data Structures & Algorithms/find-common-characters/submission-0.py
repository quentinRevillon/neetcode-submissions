class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[]
        dics_list = []

        for w in words:
            dics_list.append({})
            dic = dics_list[-1]
            for l in w:
                dic[l] = dic.get(l,0) + 1

        dic0 = dics_list[0]
        min_l_count=dic0
        for key, val in dic0.items():
            for i, dic in enumerate(dics_list):
                min_l_count[key]=min(min_l_count[key], dic.get(key, 0))

        for key, val in min_l_count.items():
            for i in range(val):
                res.append(key)

        return res

                

