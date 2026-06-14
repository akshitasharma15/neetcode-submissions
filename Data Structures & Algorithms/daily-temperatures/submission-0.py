class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result= []
        count = 0
        for i in range(len(temperatures)):
            for j in range (i +1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    count = j -i 
                    break
            result.append(count)
            count = 0
        return result
        