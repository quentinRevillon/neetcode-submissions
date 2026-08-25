class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for s in strs:
            group = anagrams_dict.get(tuple(sorted(s)), [])
            anagrams_dict[tuple(sorted(s))] = group + [s]
        print(anagrams_dict)
        groups_list = [anagrams_dict[key] for key in anagrams_dict.keys()]

        return groups_list