class Solution:
    def countBits(self, n: int) -> List[int]:
        sum_val =[]
        for i in range(n+1):
            sum_val.append(i.bit_count())
        return sum_val
        