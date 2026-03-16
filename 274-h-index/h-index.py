class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        if len(citations) <1:
            return citations[0]
        new_list = sorted(citations, reverse=True)
        for i in range(len(new_list)):
            if new_list[i] <= i :
                return i
        return len(new_list)