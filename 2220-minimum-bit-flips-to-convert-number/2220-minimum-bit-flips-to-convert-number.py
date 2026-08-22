class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        different_bits = start ^ goal
        count = 0
        while different_bits > 0:
            count += different_bits & 1
            different_bits >>= 1
        
        return count
