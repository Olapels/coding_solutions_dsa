class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #maximum steps that can be taken
        jump_reach = 0

        for i in range(len(nums)):
                if i <= jump_reach:
                    # i = how previous steps have been taken
                    # nums[i] = how much further can i go
                    jump_reach = max(jump_reach, i + nums[i])
                else:
                    #jump reach is greater, we can't move forward
                    return False
        return True
        
        