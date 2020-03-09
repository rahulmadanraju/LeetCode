# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:46:50 2020

@author: rahul
"""

class Solution:
    def twoSum(self, nums, target):
         """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {}
        
        for index, num in enumerate(nums):
            other = target - num
            
            if other in seen:
                return [seen[other], index]
            
            else:
                seen[num] = index
                
        return []