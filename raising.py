#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
**Project Name:**      
**Product Home Page:** 
**Code Home Page:**    
**Authors:**           Pengfei Cui
**Copyright(c):**      Pengfei Cui 
**Licensing:**         GPL3 
**Coding Standards:**  
Description
--------

"""

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length =length
        self.atleast=atleast

try:
    s=raw_input('Enter something -->')
    if len(s) <3:
        raise ShortInputException(len(s),3)
except EOFError:
    print '\nWhy did you do an EOF on me?'
except ShortInputException,x:
    print 'ShortInputException: The input was of length %d, \
            was expecting at least %d' % (x.length, x.atleast)
else:
    print 'No exception was raised.'

