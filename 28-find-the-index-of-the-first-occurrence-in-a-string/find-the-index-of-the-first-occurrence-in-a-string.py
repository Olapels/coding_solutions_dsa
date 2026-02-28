class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_length = len(needle)
        h_length = len(haystack)

        for alpha in range(h_length - n_length + 1):
            if haystack [alpha : alpha +n_length ] == needle:
                return alpha
        return -1
        