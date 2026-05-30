class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        prefix_array =[]
        suffix_array = []
        output= []
        for index in range(0, len(nums)):
            if index == 0:
                prefix_array.append(mul)
            else:
                mul = prefix_array[-1] * nums[index-1]
                prefix_array.append(mul)
        print(prefix_array)
        
        mul=1
        for index in range(len(nums)-1, -1, -1):
            if index == len(nums)-1:
                suffix_array.insert(0, mul)
            else:
                mul = mul * nums[index+1]
                suffix_array.insert(0, mul)
        print(suffix_array)

        for index in range(len(nums)):
            op_mul = prefix_array[index] * suffix_array[index]
            output.append(op_mul)
        
        return output


        


        


        