class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        diff_bit = xor_sum & (-xor_sum)

        a,b = 0,0

        for num in nums:
            if num & diff_bit:
                a^=num
            else:
                b^=num
        
        return [a,b]
