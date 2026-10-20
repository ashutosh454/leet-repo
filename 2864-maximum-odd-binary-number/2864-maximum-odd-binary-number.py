class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = s.count("1")
        n = len(s)

        return "1" * (count-1) + "0" * (n-count) + "1"