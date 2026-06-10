class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array = nums.sort()
        target = 0
        i = 0
        list_data = []

        while i < len(nums) - 2:
            if (i > 0) and (nums[i - 1] == nums[i]):
                i = i + 1
                continue

            diff = target - nums[i]
            output = {}
            index = i + 1
            
            while index < len(nums):
                diff_sec = diff - nums[index]
                
                if diff_sec not in output:
                    output.update({nums[index]: index})
                else:
                    list_data.append([nums[index], nums[i], diff_sec])
                    while (index < len(nums) - 1) and nums[index] == nums[index + 1]:
                        index = index + 1
                        continue
                index = index + 1
            i = i + 1

        return list_data
