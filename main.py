import fileinput

# open a file
# f1 = open('foo.txt')

# open another file to write
f2 = open('writeFile.txt', 'r')

#f3 = open('writeFile.txt', 'w')

#for line in f1:
  
      
    # looks for an empty line or comment
    #if not line or line.startswith('#'):
        #continue

    # loops through the lines in the write file
for linef2 in fileinput.FileInput('writeFile.txt', inplace=1):
    #print linef2
    linef2= linef2.strip()
    if "This" in linef2:
        #print linef2
        s = linef2.replace('This','Yeah')
        
        print s
    else:
        print (linef2)
        #f3 = open('writeFile.txt', 'w')
        
        #y = f3.write(s)
        #f3.close()
        #print y

#f3.close


    # replace 'This' with 'That' in the write file 
    #f2.write(line.replace('This', 'That'))    
    
    # write text in an empty file
    #f2.write(line)

#for line in fileinput.input('foo.txt'):
#    linename = line.strip()
#    print linename
