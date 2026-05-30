class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for i in strs:
            word += str(len(i)) + '+' + i
        return word
        

    def decode(self, s: str) -> List[str]:
        decoded_list =[]
        i =0 
        digit = ''
        while i < len(s):
            if s[i] == '+':
                decoded_list.append(s[i+1: i + int(digit) + 1])
                i += 1 + int(digit) 
                digit= ''
            else:
                digit += s[i]
                i += 1
        
        return decoded_list
        



