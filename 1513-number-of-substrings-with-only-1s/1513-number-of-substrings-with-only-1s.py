class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        current_ones = 0

        for ch in s:
            if ch == '1':
                current_ones+=1
                ans = (ans + current_ones) % MOD
            else:
                current_ones = 0

        return ans

        for block in s.split('0'):
            k = len(block)
            if k > 0:
                ans = (k*(k+1)//2) % MOD
        return ans