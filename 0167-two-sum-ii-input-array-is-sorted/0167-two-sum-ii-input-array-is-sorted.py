class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length=len(numbers)
        
        for i in range(0,length):
            low=i+1
            high=length-1
            while low<=high:
                mid=(low+high)//2
                if numbers[i]+numbers[mid]==target:
                    
                    return[i+1,mid+1]
                elif numbers[i]+numbers[mid]<=target:
                    low=mid+1
                else:
                    high=mid-1
                
        return []
        