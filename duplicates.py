# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 02:30:57 2020

@author: rahul
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums[:] = list(set(nums))
        nums.sort()
        
        
        return len(nums)
    