class Solution:
    def validStrings(self, n: int) -> List[str]:
        result=[]

        def generate(curr_str: str):
            if len(curr_str) == n:
                result.append(curr_str)
                return

            generate(curr_str + "1")

            if not curr_str or curr_str[-1] == "1":
                generate(curr_str + "0")

        generate("")
        
        return result

