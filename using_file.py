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

poem='''\
        Programming is fun
        when the work is done
        if you wanna make your work also fun:
            use Python!
            '''
f=file('poem.txt','w')
f.write(poem)
f.close()

f=file('poem.txt')
while True:
    line=f.readline()
    if len(line) == 0:
        break
    print line,
f.close()
