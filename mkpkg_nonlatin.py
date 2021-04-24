# mkpkg support module.
# search for non latin characters in input string. Return position if founded.
# see python's string.printable for more info.
# free software. (c) Eugene Mikhaylov, 2011.


import string
import sys
import re
if len(sys.argv) <= 1:
	print "Insufficient agumetns"
	sys.exit(2)
opt=sys.argv[1]
res=re.search("[^"+string.printable+"]",opt)
if res != None and len(res.group(0))>0:
    print(opt.find (res.group(0)))
