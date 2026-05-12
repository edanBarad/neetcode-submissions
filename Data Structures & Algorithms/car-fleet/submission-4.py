class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleets = []
        for p, s in combined:
            timeOfArrival = (target-p)/s
            if not fleets or timeOfArrival > fleets[-1]:
                fleets.append(timeOfArrival)

        return len(fleets)