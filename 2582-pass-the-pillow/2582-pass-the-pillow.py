class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = n-1

        rem_time = time % (2*cycle_length)

        if rem_time < cycle_length:
            return rem_time+1
        else:
            return n-(rem_time - cycle_length)