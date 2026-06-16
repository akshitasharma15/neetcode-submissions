class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # index = -1

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         index = i 
        #         return index
        
        # return index
        l = 0
        r = len(nums) - 1 

        while l <= r:
            mid_ele = l + ((r - l) // 2) 

            if nums[mid_ele] == target:
                return mid_ele

            elif nums[mid_ele] < target:
                l = mid_ele + 1
            else:
                r = mid_ele - 1
        
        return -1
