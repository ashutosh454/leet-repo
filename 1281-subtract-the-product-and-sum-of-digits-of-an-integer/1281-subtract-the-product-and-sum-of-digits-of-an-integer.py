class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def productOfDigits(num):
            nums = num
            pro = 1
            while num>0:
                rem = num%10
                pro = pro*rem
                num = num//10
            return pro
        
        def sumOfDigits(num):
            nums = num
            sum1 = 0
            while num>0:
                rem = num%10
                sum1 = sum1+rem
                num= num//10
            return sum1

        product = productOfDigits(n)
        sum1 = sumOfDigits(n)
        return product-sum1

