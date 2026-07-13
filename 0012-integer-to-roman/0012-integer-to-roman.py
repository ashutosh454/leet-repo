class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result=[]
        
        for value,symbol in numerals:
            if num==0:
                break
            count=num//value
            if count>0:
                result.append(symbol*count)
                num%=value
        return "".join(result)