class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x, y = zip(*sorted(zip(position, speed)))
        cars = list(x)
        speeds = list(y)
        stack = []
        for i in range(len(cars)-1, -1, -1):
            car = cars[i]
            time_taken = float((target - car) / speeds[i])
            if stack and stack[-1] >= time_taken:
                continue
            stack.append(time_taken)
        return len(stack)
