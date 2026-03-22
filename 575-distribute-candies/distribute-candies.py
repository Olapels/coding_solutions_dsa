class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        u_candies = len(set(candyType))

        max_candies = len(candyType) // 2

        return min(max_candies, u_candies)

        