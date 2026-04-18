class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        bit_element=0
        for i in range(n):
            current = start+2*i
            bit_element ^= current
        return bit_element
        