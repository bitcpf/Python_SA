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
Back up all the files in the list
"""

import os
import time
# The files and directories to be backed up are specified in a list
source = ['/home/pcui/bitcpf/instrument/', '/home/pcui/bitcpf/ppt/']

target_dir = '/home/pcui/bitcpf/instrument/backuptest/'

today = target_dir +time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = raw_input('Enter a comment---> ')

if len(comment) ==0:
    target = today + os.sep + now +'.zip'
else:
    target = today + os.sep + now + '_'\
            +comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

#target = today + os.sep + now + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) ==0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'


