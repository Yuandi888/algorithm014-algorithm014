
# 66. Plus One
# 66. 加一

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        # 只有一位的情况
        if n == 1 and digits[0] == 9:
            digits[0] = 0
            digits = [1] + digits
        elif n == 1 and digits[0] != 9:
            digits[0] += 1
        # 有多位的情况
        elif n > 1:

            # 从右往左遍历，到第一位之前
            for i in range(n-1,0,-1):
                if digits[i] + carry != 10:
                    digits[i] += carry
                    carry = 0
                    return digits
                elif digits[i] + carry == 10:
                    digits[i] = 0
                    carry = 1

            # 第一位单独处理
            if digits[0] + carry != 10:
                digits[0] += carry
            else:
                digits[0] = 0
                digits = [1] + digits
                
        return digits
