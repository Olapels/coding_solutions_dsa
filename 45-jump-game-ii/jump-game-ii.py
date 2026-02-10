class Solution:
    def jump(self, nums: list[int]) -> int:
        n_jumps = 0
        current_jump_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_jump_end:
                n_jumps += 1            
                current_jump_end = farthest  
                
        return n_jumps