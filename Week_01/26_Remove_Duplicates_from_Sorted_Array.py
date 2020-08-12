#26. Remove Duplicates from Sorted Array
#26. 删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i+1