import fileinput

for line in fileinput.FileInput('foo.txt'):
  
      
    # looks for an empty line or comment
    if not line or line.startswith('#'):
        continue
        
    if "Erica" in line:

    # loops through the lines in the write file
        for linef2 in fileinput.FileInput('writeFile.txt', inplace=1):
    
            linef2= linef2.strip()
            if "Gaga" in linef2:
                line = line.strip()
                s = linef2.replace('Gaga',line)
                print s
            else:
                print linef2
           
