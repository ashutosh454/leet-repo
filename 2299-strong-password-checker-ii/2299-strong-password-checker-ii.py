class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        has_lower = False
        has_upper = False
        has_digit = False
        has_specialChar = False

        special_char = set("!@#$%^&*()-+")

        for i in range(len(password)):
            if i > 0 and password[i] == password[i-1]:
                return False
            char = password[i]

            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
            elif char in special_char:
                has_specialChar = True
        return has_lower and has_upper and has_digit and has_specialChar
