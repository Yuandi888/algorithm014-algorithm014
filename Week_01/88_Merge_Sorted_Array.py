# 88. Merge Sorted Array
# 88. 合并两个有序数组

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m+n-1
        end_1 = m-1
        end_2 = n-1
        while(end_1>=0 and end_2>=0):
        	if nums1[end_1] >= nums2[end_2]:
        		nums1[end] = nums1[end_1]
        		end_1 -= 1
        	else:
        		nums1[end] = nums2[end_2]
        		end_2 -= 1
        	end -= 1
        nums1[:end_2+1] = nums2[:end_2+1]