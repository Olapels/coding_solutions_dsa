     
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #using hashmaps
        value_counts = {}

        for num in nums:
            #increment value of the key if duplicate found
            if num in value_counts:
                value_counts[num] += 1
            #the first value of each key will start with one
            else:
                value_counts[num] = 1

        #return the key not the max value counts itself
        return max(value_counts, key=value_counts.get)