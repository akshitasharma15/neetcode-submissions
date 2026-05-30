class Solution:
    def isValid(self, s: str) -> bool:
        list_ele = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                list_ele.append(i)
            elif i == ')' and len(list_ele) != 0 and list_ele[-1] == '(':
                list_ele.pop()
            elif i == '}' and len(list_ele) != 0 and list_ele[-1] == '{':
                list_ele.pop()
            elif i == ']' and len(list_ele) != 0 and list_ele[-1] == '[':
                list_ele.pop()
            else:
                return False
        
        return True if not list_ele else False


