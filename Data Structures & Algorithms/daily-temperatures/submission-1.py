class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result= []
        # count = 0
        # for i in range(len(temperatures)):
        #     for j in range (i +1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             count = j -i 
        #             break
        #     result.append(count)
        #     count = 0
        # return result

        result = [0] * (len(temperatures))
        new_stack = []

        for i in range(len(temperatures)):
            if not new_stack:
                new_stack.append(i)
            else:       
                while new_stack and (temperatures[i] > temperatures[new_stack[-1]]):
                    result[new_stack[-1]] = i - new_stack[-1]
                    new_stack.pop()
                new_stack.append(i)
        
        return result

        