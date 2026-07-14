from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts=Counter(ransomNote)
        magazine_counts=Counter(magazine)

        return ransom_counts<=magazine_counts
           