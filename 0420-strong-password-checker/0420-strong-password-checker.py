class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)

        missing_types = 3-(has_lower + has_upper + has_digit)

        n = len(password)

        repeat =[]
        i=0
        while i<n:
            j=i
            while j<n and password[j] == password[i]:
                j+=1
            length =j-i
            if length >=3:
                repeat.append(length)
            i=j
        
        if n<6:
            return max(6-n, missing_types)
        elif n <=20:
            replacements = sum(length//3 for length in repeat)
            return max(replacements, missing_types)
        else:
            deletions = n-20
            left_to_delete = deletions

            for idx, length in enumerate(repeat):
                if left_to_delete>0 and length%3 ==0:
                    repeat[idx]-=1
                    left_to_delete-=1
            for idx, length in enumerate(repeat):
                if length%3==1 and left_to_delete > 0:
                    rem =min(left_to_delete , 2)
                    repeat[idx]-=rem
                    left_to_delete-=rem

            for idx,length in enumerate(repeat):
                if length>=3 and left_to_delete > 0:
                    possible_del = repeat[idx] -2
                    rem = min(left_to_delete, possible_del)
                    repeat[idx]-=rem
                    left_to_delete-=rem
            replacements = sum(length//3 for length in repeat)

            return deletions + max(replacements , missing_types)


                    