class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        if zero_count > 1:
            return [0] * n 
        elif zero_count == 1:
            result = [0] * n
            zero_index = nums.index(0)
            result[zero_index] = product  # product holds the product of non-zero elements
            return result
        else: 
            result = [product // num for num in nums]
            return result





        