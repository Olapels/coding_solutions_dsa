class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        if len(citations) <1:
            return citations[0]
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] <= i :
                return i
        return len(citations)