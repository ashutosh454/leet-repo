class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if not height:
            return 0
        i=0
        j=n-1

        left_max = [0]*n
        right_max = [0]*n

        left_max[i] = height[0]
        right_max[j]= height[n-1]
        
        for i in range(1,n):
            left_max[i] = max(left_max[i-1] , height[i])
        for j in range(n-2,-1,-1):
            right_max[j] = max(right_max[j+1], height[j])
        total_water =0
        for i in range(n):
            total_water+= (min(left_max[i],right_max[i])-height[i])
        
        return total_water

