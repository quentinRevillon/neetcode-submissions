class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        array = [(heights[i], names[i]) for i in range(len(names))]
        array.sort(key=lambda x: -x[0])
        return [array[i][1] for i in range(len(array))]

        