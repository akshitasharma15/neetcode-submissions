class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = {}
        count = 1

        for i, j in enumerate(nums):
            if num=={}:
                num.update({j:count})
            elif j in num:
                num[j] += 1
            
            else:
                num.update({j:count})

        for i in num:
            if num[i] >1:
                return True
        
        return False



        