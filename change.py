import fileinput
import subprocess
import sys

# takes the first command line argument as the file to find values to be modified 
for line in fileinput.FileInput(sys.argv[1]):
  
      
    # looks for an empty line or comment
    if not line or line.startswith('#'):
        continue
    
    # gets rid of blank spaces
    line = line.strip()
    #print line

    s = line.split(" ", 1)[0]
    #print s
    for line2 in fileinput.FileInput('constants.h', inplace =1):
        if s in line2:
           line2 = line2.strip()
           sp = line2.split(s,1)[0]
           # print sp
           seq = ["\t",sp, line, ";"]
           str = ""
           sp = str.join(seq) 
           print sp.rstrip()
        else:
            print line2.rstrip()

subprocess.call("make")
subprocess.call(["make","clean"])
#print sys.argv[1]
