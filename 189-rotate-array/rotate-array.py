class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0: return
        k %= n
        if k == 0: return
        nums[:] = nums[-k:] + nums[:-k]