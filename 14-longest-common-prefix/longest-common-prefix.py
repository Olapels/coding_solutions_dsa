class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sorted_strs = sorted(strs)
        prefix = []

        first,last = sorted_strs[0], sorted_strs[-1]
        for i in range(len(first)):
            if first[i] == last[i]:
                prefix.append(last[i])
            else:
                return "".join(prefix)
            
        return "".join(prefix)
        