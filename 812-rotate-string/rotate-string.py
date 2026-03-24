class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        counter = 0
        while counter < len(s):
            for val in s:
                s = s[1:] + s[0]
                counter+=1
                if s == goal:
                    return True
            return False
        