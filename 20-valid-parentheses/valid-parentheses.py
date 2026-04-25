class Solution:
    def isValid(self, s: str) -> bool:
        valid_parent = {'()', '{}', '[]'}
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack or stack[-1]+char not in valid_parent:
                    return False
                stack.pop()
        return not stack