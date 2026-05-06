class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]]
        for i in range(1, len(height)):
            left.append(max(left[i-1], height[i]))
        right = [height[-1]]
        for i in range(1, len(height)):
            right.append(max(right[i-1], height[-i-1]))
        right.reverse()
        total = 0
        for i in range(len(height)):
            total += min(left[i], right[i]) - height[i]
        return total