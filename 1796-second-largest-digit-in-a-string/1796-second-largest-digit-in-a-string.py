class Solution:
    def secondHighest(self, s: str) -> int:
        largest=-1
        second_largest=-1

        for char in s:
            if char.isdigit():
                val = int(char)

                if val>largest:
                    second_largest = largest
                    largest=val
                elif val < largest and val> second_largest:
                    second_largest = val
        return second_largest