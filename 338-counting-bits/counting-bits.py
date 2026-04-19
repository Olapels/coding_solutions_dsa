class Solution:
    def countBits(self, n: int) -> List[int]:
        sum_val =[]
        for i in range(n+1):
            sum_val.append(sum(int(d) for d in bin(i)[2:]))
        return sum_val
        