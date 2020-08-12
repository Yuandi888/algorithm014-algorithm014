# 189. Rotate Array
# 189. 旋转数组


# 三次反转法
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        nums[:] = nums[::-1] #反转整体
        nums[:k] = nums[:k][::-1] #反转第二段
        nums[k:] = nums[k:][::-1] #反转第一段
        return nums


# 切片
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        nums[:] = nums[length-k:] + nums[:length-k]
        return nums


# 直接交换
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        if k == 0:
        	return
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
        return nums