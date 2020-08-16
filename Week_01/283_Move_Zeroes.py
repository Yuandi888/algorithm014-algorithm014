# 283. Move Zeroes
# 283. 移动零


# 利用双指针while循环
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        j = 1
        while j <= n-1:
            if nums[i] == 0 and nums[j] == 0:
                j += 1
            elif nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] != 0:
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] == 0:
                i += 1
                j += 1
        return nums



# 利用双指针for循环
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for j in range(n)
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[i] != 0:
                i += 1
        return nums






