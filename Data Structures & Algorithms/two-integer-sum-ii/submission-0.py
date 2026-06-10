class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = {}


        for index, value in enumerate(numbers):
            diff = target - value

            if diff in output:
                return[output[diff], index +1]

            if diff not in output:
                output.update({value:index+1}) 
       