class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                maxi = max(maxi, area)
        return maxi
