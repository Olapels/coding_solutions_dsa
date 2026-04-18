class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced=split = 0
        for x in range(len(s)):
            if s[x] =='L':
                balanced+=1
            else:
                balanced-=1
            if balanced==0:
               split+=1 
        return split 
        