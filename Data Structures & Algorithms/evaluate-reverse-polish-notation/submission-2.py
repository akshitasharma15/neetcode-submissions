class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        new_stack = []
        for i in tokens:
            if i not in ("+", "*", "-", "/"):
                new_stack.append(int(i))
            
            elif i in  ("+", "*", "-", "/"):
                a = new_stack.pop()
                b = new_stack.pop()
                
                if i == "+":
                    val = b + a
                elif i == "*":
                    val = b * a
                elif i == "-":
                    val = b - a
                else:
                    val = b / a
                new_stack.append(int(val))

        return new_stack[0]

