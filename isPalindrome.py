# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:46:50 2020

@author: rahul
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        rev = 0
        
        temp = x
        rev = 0
 
        while temp != 0:
	        rev = (rev * 10) + (temp % 10)
	        temp = temp // 10
 
        if x == rev:
	        print("true")
        else:
	        print("false")