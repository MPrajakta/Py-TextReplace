import fileinput

for line in fileinput.FileInput('change.txt'):
  
      
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
"""
    if "CTA_SIZE" in line:

    # loops through the lines in the write file
       for linef2 in fileinput.FileInput('constants.h', inplace=1):
    
            
            if "CTA_SIZE" in linef2:
                linef2 = linef2.strip()
                line = line.strip()
                s = linef2.split("CTA_SIZE", 1)[0]
                str = ""
                seq = ["\t",s, line,";"]
                s = str.join(seq)
                print s.rstrip()
            else:
                print linef2.rstrip()
    """
