import fileinput

for line in fileinput.FileInput('change.txt'):
  
      
    # looks for an empty line or comment
    if not line or line.startswith('#'):
        continue
        
    if "CTA_SIZE" in line:

    # loops through the lines in the write file
        for linef2 in fileinput.FileInput('constants.h', inplace=1):
    
            linef2= linef2.strip()
            if "CTA_SIZE" in linef2:
                line = line.strip()
                s = linef2.split("CTA_SIZE", 1)[0]
                str = " "
                seq = [s, line]
                s = str.join(seq)
                print s
            else:
                print linef2
           
