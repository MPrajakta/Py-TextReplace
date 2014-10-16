import fileinput

f1 = open('foo.txt')
#f2 = open('foo.txt.tmp', 'w')

for line in f1:
    print "This is a line"
    linename = line.strip()
    if not linename or linename.startswith('#'):
        continue
#    f1.write(line.replace('This', 'That'))    
    #print linename 

#for line in fileinput.input('foo.txt'):
#    linename = line.strip()
#    print linename
