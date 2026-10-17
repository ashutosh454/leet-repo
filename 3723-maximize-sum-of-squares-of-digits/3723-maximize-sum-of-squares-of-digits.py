class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*9 < sum:
            return ""
        
        nine = sum // 9
        rem = sum % 9

        ans = ["9"]*nine
        if rem > 0:
            ans.append(str(rem))

        while len(ans) < num:
            ans.append("0")
        
        return "".join(ans)