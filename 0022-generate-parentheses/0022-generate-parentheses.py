class Solution:
    def generate(self, index, total, brackets, n, result):
        
        if index == n * 2:
            if total == 0:
                result.append("".join(brackets))
            return

        
        if total < 0 or total > n:
            return

        
        brackets[index] = "("
        self.generate(index + 1, total + 1, brackets, n, result)

        
        brackets[index] = ")"
        self.generate(index + 1, total - 1, brackets, n, result)

    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        brackets = [""] * (2 * n)  
        self.generate(0, 0, brackets, n, ans)
        return ans