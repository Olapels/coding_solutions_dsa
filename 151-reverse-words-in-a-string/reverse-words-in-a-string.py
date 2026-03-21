class Solution:
    def reverseWords(self, s: str) -> str:
        ns = s.strip().split()[::-1]
        return " ".join(ns)