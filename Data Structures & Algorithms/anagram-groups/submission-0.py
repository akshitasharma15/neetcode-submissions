class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for index, value in enumerate(strs):
            count = [0] * 26
            for i in value:
                index_strs = ord(i) - ord('a')
                count[index_strs] += 1

            output[tuple(count)].append(value)
        return list(output.values())




