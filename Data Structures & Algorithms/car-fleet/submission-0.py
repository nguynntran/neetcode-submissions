class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = []
        for i in range(len(position)):
            car_fleet.append([position[i], speed[i]])
        car_fleet = sorted(car_fleet)[::-1]
        count = 0
        stack = []
        for pos, spe in car_fleet:
            stack.append((target - pos) / spe)
            if len(stack) >= 2 and (stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)