# 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
# 思路：把数组从中间拆分为左右两部分，如果左半边数组是有序的，那无序部分就在右半部分，以此类推，每次减半，最后找到无序的位置。

class Solution:
    def findDisorder(self, array: List[int]) -> bool:
        left_idx = 0
        right_idx = len(array) - 1
        while right_idx - left_idx > 1:
            mid_idx = (left_idx + left_idx) // 2
            if array[left_idx] < array[(left_idx+mid_idx)//2] and array[(left_idx+mid_idx)//2] < array[mid_idx]:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx
        return [array[left_idx], array[right_idx]]