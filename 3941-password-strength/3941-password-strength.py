class Solution:
    def passwordStrength(self, password: str) -> int:
        unique_char = set(password)
        strength=0
        special_char = {'!','@','#','$'}

        for char in unique_char:
            if char.islower():
                strength +=1
            elif char.isupper():
                strength+=2
            elif char.isdigit():
                strength+=3
            elif char in special_char:
                strength+=5
        return strength
