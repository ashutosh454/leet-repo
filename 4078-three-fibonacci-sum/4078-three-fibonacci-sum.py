fib_set = set()
a,b = 0,1
while b<= 10**9:
    fib_set.add(b)
    a,b = b , a+b
class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        return n % 2 == 0 and (n//2) in fib_set
        