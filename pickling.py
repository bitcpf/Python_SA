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

import cPickle as p

shoplistfile= 'shoplist.data'

shoplist = ['apple','mango','carrot']

f=file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()

del shoplist

f=file(shoplistfile)
storedlist=p.load(f)

print storedlist
