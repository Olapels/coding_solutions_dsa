class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 'i' is the index of the last unique element found
        i = 0
        
        # 'j' checks the rest of the array
        for j in range(1, len(nums)):
            # If we find a new unique value
            if nums[j] != nums[i]:
                #we found a unique value, increment i
                i += 1
                # Move the unique value to the next available slot
                nums[i] = nums[j]
        
        # Return the count of unique elements (index + 1)
        return i + 1