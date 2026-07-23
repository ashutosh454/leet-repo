from collections import Counter
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) ->int:
            min_string = min(s)
            return s.count(min_string)

        word_score = sorted(f(w) for w in words)
        n=len(word_score)

        result = []

        for q in queries:
            query_score = f(q)
            idx = bisect.bisect_right(word_score , query_score)
            result.append(n-idx)
        return result
        