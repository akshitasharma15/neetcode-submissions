class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unique_s={}
        unique_t={}

        # if len(s) != len(t):
        #     return False

        for i, j in enumerate(s):
            if j in unique_s:
                unique_s[j]+= 1
            else:
                unique_s.update({j:1})
        
        for i,j in enumerate(t):
            if j in unique_t:
                unique_t[j] += 1
            else:
                unique_t.update({j:1})  

        if unique_s == unique_t:
            return True

        return False     


        