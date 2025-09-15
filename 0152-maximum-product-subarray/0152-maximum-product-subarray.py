class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            # If current number is negative, swap max_so_far and min_so_far
            if curr < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            # Update max and min products for the current position
            max_so_far = max(curr, max_so_far * curr)
            min_so_far = min(curr, min_so_far * curr)
            
            # Update the overall result
            result = max(result, max_so_far)
            
        return result