class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        output=[]
        for i in nums:
            if i in mapping:
                mapping[i] += 1
            else:
                mapping.update({i:1})
        
        if len(mapping) == 1:
            return list(mapping.keys())
        
        for i, j in sorted(mapping.items(), key=lambda item: item[1], reverse = True):
            if not k>0:
                break

            output.append(i)
            k -= 1
        return output
    

           



        