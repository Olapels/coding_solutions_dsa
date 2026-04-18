class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        div_num = []

        for x in range(left,right+1):
            if all(int(d) != 0 and x % int(d) == 0 for d in str(x)):
                div_num.append(x)
        
        return div_num