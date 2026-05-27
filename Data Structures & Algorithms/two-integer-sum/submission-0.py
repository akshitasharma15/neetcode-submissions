class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        output = []

        for i, k in enumerate(nums):
            j = len(nums)-1
            while i < j:
                sum = nums[i] + nums[j]                
                if sum == target:
                    output.append(i)
                    output.append(j)
                    return output
                
                j = j-1
        
        return output