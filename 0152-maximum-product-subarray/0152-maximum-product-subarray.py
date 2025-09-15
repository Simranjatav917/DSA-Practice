class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            # The maximum and minimum products can become
            # `current_element`, `current_element * max_so_far`
            # or `current_element * min_so_far`.
            
            # A temporary variable is needed because max_so_far's
            # value is required to calculate the new min_so_far.
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            
            max_so_far = temp_max
            
            result = max(result, max_so_far)
            
        return result