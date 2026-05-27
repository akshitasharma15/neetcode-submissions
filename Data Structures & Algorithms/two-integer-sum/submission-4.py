class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        output={}

        for index, value  in enumerate(nums):
            diff = target - value
            print(diff)
            
            if diff in output:
                return[output[diff], index]

            if diff not in output:
                output.update({value:index})

        return []
            




