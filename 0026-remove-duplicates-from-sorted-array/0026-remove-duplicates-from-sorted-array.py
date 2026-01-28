class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_v0 = []
        for i in nums: 
            if i not in nums_v0:
                nums_v0.append(i)
        
        nums[:] = nums_v0
        
        return len(nums)