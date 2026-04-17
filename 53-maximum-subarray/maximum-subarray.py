class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        current_max=nums[0]
        maximum=nums[0]
        for x in range(1,len(nums)):
            current_max =max(nums[x], current_max+ nums[x])
            if current_max > maximum:
                maximum = current_max

        return maximum

        
        