class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        new_stack =[]
        mapping = [[p,s] for p, s in zip(position, speed)]
        mapping.sort(reverse=True)

        for p, s in mapping:
            time_taken = ((target - p) / s)
            if not new_stack or time_taken > new_stack[-1]:
                new_stack.append(time_taken)
        
        return len(new_stack)

        
        