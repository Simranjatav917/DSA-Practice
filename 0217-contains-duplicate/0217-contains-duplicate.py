class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_hash_map = {}
        for num in nums:
            if num in my_hash_map:
                return True
            my_hash_map[num] = True
        return False

        