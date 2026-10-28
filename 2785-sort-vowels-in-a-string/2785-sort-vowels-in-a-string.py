class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        sorted_vowels = sorted([c for c in s if c in vowels])

        result = []
        v_idx =0

        for c in s:
            if c in vowels:
                result.append(sorted_vowels[v_idx])
                v_idx+=1

            else:
                result.append(c)
        
        return "".join(result)