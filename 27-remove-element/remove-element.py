class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        n = len(nums)
        
        while pointer < n:
            #if the current value at nums is the same as val
            if nums[pointer] == val:
                # Replace it with the last value from nums
                nums[pointer] = nums[n - 1]
                #reduce the size of what we check
                n -= 1
            else:
                # if the value is not the same, just skip and move forward
                pointer += 1  
        return n