class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1.0
        if n==1:
            return x
        
        if n < 0:
            x = 1 / x
            n = -n
            
        
        half = self.myPow(x, n // 2)
        
        
        if n % 2 == 1:
            return half * half * x
        else:
            return half * half