import fileinput

for line in fileinput.FileInput('change.txt'):
  
      
    # looks for an empty line or comment
    if not line or line.startswith('#'):
        continue
        
    if "CTA_SIZE" in line:

    # loops through the lines in the write file
        for linef2 in fileinput.FileInput('constants.h', inplace=1):
    
            #inef2 = linef2.strip(); 
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
    elif "NUM_SIZE" in line:
        print line
        for line2 in fileinput.FileInput('constants.h', inplace =1):
            if "NUM_SIZE" in line2:
                line2 = line2.strip()
                line =line.strip()
                s = line2.split("NUM_SIZE", 1)[0]
                str =""
                seq = ["\t", s, line, ";"]
                s=str.join(seq)
                print s.rstrip()
            else:
                print line2.rstrip()
