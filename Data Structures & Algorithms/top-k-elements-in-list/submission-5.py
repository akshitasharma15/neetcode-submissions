class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        output=[]
        freq =[[] for i in range(len(nums) + 1)]
        for i in nums:
            if i in mapping:
                mapping[i] += 1
            else:
                mapping.update({i:1})
        
        for key, value in mapping.items():
            freq[value].append(key)
        
        for num in range(len(freq) -1 , 0, -1):
            for j in freq[num]:
                output.append(j)
                if len(output) == k:
                    return output
    

           



        