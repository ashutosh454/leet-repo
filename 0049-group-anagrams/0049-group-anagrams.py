from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anargam_map={}
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in anargam_map:
                anargam_map[sorted_word] = []
            anargam_map[sorted_word].append(word)

        return list(anargam_map.values())

        