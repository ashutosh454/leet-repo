class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left_sum = sum(cardPoints[:k])
        right_sum = 0
        max_score = left_sum

        left_idx = k-1
        right_idx = n-1

        for _ in range(k):
            left_sum -= cardPoints[left_idx]
            right_sum += cardPoints[right_idx]

            max_score = max(left_sum+right_sum, max_score)

            left_idx -=1
            right_idx -=1
        
        return max_score

