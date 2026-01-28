class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_reach = 0

        for i in range(len(nums)):
                if i <= jump_reach:
                    jump_reach = max(jump_reach, i + nums[i])
                else:
                    return False
        return True
        
        