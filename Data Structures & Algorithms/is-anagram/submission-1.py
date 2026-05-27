class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 1
        unique_s={}
        unique_t={}

        if len(s) != len(t):
            return False

        for i, j in enumerate(s):
            if j in unique_s:
                unique_s[j]= count + 1
            else:
                unique_s.update({j:count})
        
        for i,j in enumerate(t):
            if j in unique_t:
                unique_t[j]= count +1
            else:
                unique_t.update({j:count})  

        if  unique_s == unique_t:
            return True

        return False     


        