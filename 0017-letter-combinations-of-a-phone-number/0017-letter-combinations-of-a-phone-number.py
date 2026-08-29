class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def generate(index, current_path):
            if index == len(digits):
                result.append("".join(current_path))
                return
            
            possible_letter = digit_to_letters[digits[index]]

            for letters in possible_letter:
                current_path.append(letters)
                generate(index+1, current_path)
                current_path.pop()

        generate(0,[])
        return result