from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def dfs(freq_map : Counter):
            total_sequence = 0

            for char,freq in freq_map.items():
                if freq == 0:
                    continue
                
                total_sequence+=1

                freq_map[char]-=1
                total_sequence += dfs(freq_map)

                freq_map[char] += 1
            return total_sequence
        return dfs(count)

                
        