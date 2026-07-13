class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def get_next(num: int) -> int:
            total_sum =0
            while num >0:
                digit = num%10
                total_sum+=digit**2
                num=num//10
            return total_sum
        while n!=1:
            n = get_next(n)

            if n in seen:
                return False
            seen.add(n)
        return True

        