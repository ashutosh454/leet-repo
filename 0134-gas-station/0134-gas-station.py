class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1

        total_tank = 0
        starting_station = 0

        for i in range(len(gas)):
            total_tank += gas[i]-cost[i]

            if total_tank<0:
                starting_station = i+1
                total_tank = 0

        return starting_station
        