class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        # 10 8 5 3 0
        # 2  4 1 3 1
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target-p)/s)
            # 1 7 12

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


            



        