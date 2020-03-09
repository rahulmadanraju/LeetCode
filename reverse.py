# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:46:50 2020

@author: rahul
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = str(x)
        
        if y[0] == '-':
            z = int('-' + y[-1:0:-1])
        
        elif y[-1] == '0':
            z = int(y[::-1])
        
        else:
            
            z = y[::-1]
        
        return z