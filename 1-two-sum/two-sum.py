class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_num = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in previous_num:
                return(i, previous_num[difference])
            previous_num[n] = i
            