f=open('hello_world.txt','r')
#to access any file, first the 'open' command needs to be used
#the file name to be open needs to be in the same directory the current program is being executed
for line in f:
    x=line[0:4]
    print x