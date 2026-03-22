class Solution:
    def binaryGap(self, n: int) -> int:
        binary = format(n,'b')
        dis = 0
        last_pos = None

        for i, val in enumerate(binary):
            if val =='1':
                if last_pos!=None:
                    dis = max(dis, i-last_pos)
                last_pos = i
        return dis

        