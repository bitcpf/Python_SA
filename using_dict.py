#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
**Project Name:**      
**Product Home Page:** 
**Code Home Page:**    
**Authors:**           
**Copyright(c):**      Pengfei Cui 
**Licensing:**         GPL3 
**Coding Standards:**  
Description
--------

"""

ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
             'Larry'     : 'larry@wall.org',
             'Matsumoto' : 'matz@ruby-lang.org',
             'Spammer'   : 'spammer@hotmail.com'
     }

print "Swaroop's address is %s" % ab['Swaroop']

ab['Guido']='guido@python.org'

del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)

for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)

if 'Guido' in ab:
    print "\nGuido's address is %s" % ab['Guido']


