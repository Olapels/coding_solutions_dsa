class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead
        """
        n = len(nums)
        if n == 0 or k % n == 0:
            return

        #reduce k to the modular division output of k%n if k >n
        k %= n

        new_nums = [0] * n
        #first k elements on new list from the back k element
        new_nums[:k] = nums[-k:]
        #onward from position k up till the -k
        new_nums[k:] = nums[:-k]

        nums[:] = new_nums
