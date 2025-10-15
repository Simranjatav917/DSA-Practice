class Solution(object):
    def findDuplicate(self, nums):
        maph={}
        for num in nums:
           maph[num] = maph.get(num, 0) + 1
        for num,count in maph.items():
            if  maph[num] >1:
                return num 
        return -1        

        