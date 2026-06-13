class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_val = nums.sort()
        count = 1
        max_value = 1

        if not nums:
            return 0

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] +1:
                count +=1

            elif nums[i+1] == nums[i]:
                continue

            else:
                max_value = max(max_value, count)
                count = 1

        return max(max_value, count)






        