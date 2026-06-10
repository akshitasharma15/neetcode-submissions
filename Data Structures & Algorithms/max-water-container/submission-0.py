class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) -1 
        max_height = 0
        i = 0

        while(i<j):
            
            calc_height = (j-i) * min(heights[j], heights[i])
            
            if calc_height > max_height: 
                max_height = calc_height
            
            if heights[j] > heights[i]:
                i +=1
            else:
                j -=1
        return max_height

        