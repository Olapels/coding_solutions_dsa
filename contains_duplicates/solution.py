from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #edge case
        if len(nums) > 0 and len(nums) <= 1:
            return False
        #initialize an empty set
        set_array = set()
        for num in nums:
            #break out early if duplicate is found
            if num in set_array:
                return True
            set_array.add(num)
        #just return false after adding all values if no duplicate found
        return False
            