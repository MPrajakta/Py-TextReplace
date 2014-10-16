import fileinput

# open a file
f1 = open('foo.txt')

# open another file to write
f2 = open('writeFile.txt', 'w')

for line in f1:
    #print "This is a line"
    #linename = line.strip()
    
    # looks for an empty line or comment
    if not line or line.startswith('#'):
        continue
    #f1.write(line.replace('This', 'That'))    
    
    # write text in an empty file
    f2.write(line)

#for line in fileinput.input('foo.txt'):
#    linename = line.strip()
#    print linename
