class Solution:
    def numberOfChild(self, n: int, time: int) -> int:
        cycle_length = n-1
        rem_time = time% (2*cycle_length)

        if rem_time < cycle_length:
            return rem_time
        else:
            return (n-1)-(rem_time -cycle_length)