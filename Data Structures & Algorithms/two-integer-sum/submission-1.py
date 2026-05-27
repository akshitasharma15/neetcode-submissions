class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, k in enumerate(nums):
            j = len(nums)-1
            while i < j:
                sum = nums[i] + nums[j]                
                if sum == target:
                    return [i,j]
                
                j = j-1
        
        return output