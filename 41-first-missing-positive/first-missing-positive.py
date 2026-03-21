class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sorted_list = sorted(set([x for x in nums if x>0]))
        counter = 0
        if not sorted_list:
            return 1
        for num in sorted_list:
            counter+=1
            if num > counter:
                return counter
        return counter + 1

        