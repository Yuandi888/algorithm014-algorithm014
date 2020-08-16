# 42. Trapping Rain Water
# 42. 接雨水

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0 #水量
        maxLeft = 0 #左边最高的
        maxRight = 0 #右边最高的
        i = 0 #左指针
        j = n - 1 #右指针
        # 从左右两边向中间遍历，每次较矮的一头的指针往里移动一位
        while i <= j:
            if maxLeft <= maxRight:
                if height[i] < maxLeft:
                    water += maxLeft - height[i]
                elif height[i] > maxLeft:
                    maxLeft = height[i]
                i += 1
            elif maxLeft > maxRight:
                if height[j] < maxRight:
                    water += maxRight - height[j]
                elif height[j] > maxRight:
                    maxRight = height[j]
                j -= 1
        return water