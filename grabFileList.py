#!/usr/bin/python3.5

import sys
import subprocess
import os

storage = []

for root, directories, filenames in os.walk('/some/path/to/use/as/root'):
    [ storage.append(os.path.join(root,filename)) for filename in filenames ]

theFile = open("output.txt","w")
for item in storage:
  theFile.write("%s\n" % item)        
theFile.close()  
