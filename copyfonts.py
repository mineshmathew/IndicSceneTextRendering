import sys
import shutil
fontList=[]
with open(sys.argv[1]) as fp:
    for line in fp:
	#print line
   	if 1:    
		#print line
		splitted=line.split(":")
		#print splitted[1]
		fontPath= splitted[0]
		shutil.copy2(fontPath,'.')
