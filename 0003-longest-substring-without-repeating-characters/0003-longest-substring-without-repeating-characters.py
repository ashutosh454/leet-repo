class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict={}
        right=0
        left=0
        maximum=0

        while right<len(s):
            if s[right] in my_dict:
                left = max(left,my_dict[s[right]]+1)
            maximum = max(maximum,(right-left+1))
            my_dict[s[right]] = right
            right+=1
        return maximum