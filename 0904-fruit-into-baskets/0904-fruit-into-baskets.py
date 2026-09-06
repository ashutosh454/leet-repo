class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket={}
        left = 0
        maximum = 0

        for right in range(len(fruits)):
            curr_fruit = fruits[right]
            basket[curr_fruit] = basket.get(curr_fruit,0)+1

            if len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit]-=1
                if basket[left_fruit] == 0:
                    del(basket[left_fruit])
                left+=1
            maximum = max(maximum,right-left+1)

        return maximum