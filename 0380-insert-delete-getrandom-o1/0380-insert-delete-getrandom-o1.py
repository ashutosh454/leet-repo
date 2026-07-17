import random
class RandomizedSet:

    def __init__(self):
        self.nums_list=[]
        self.pos_map={}

    def insert(self, val: int) -> bool:
        if val in self.pos_map:
            return False
        
        self.pos_map[val] = len(self.nums_list)
        self.nums_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos_map:
            return False

        idx_to_remove = self.pos_map[val]
        last_element = self.nums_list[-1]

        self.nums_list[idx_to_remove] = last_element
        self.pos_map[last_element] = idx_to_remove

        self.nums_list.pop()
        del self.pos_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()