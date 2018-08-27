from sys import argv
script,filename=argv
print "we are going to delete this file %r" %filename
print "if you don't want to delete then press ctrl+c"
print "if you want to proceed then hit return"
file=open(filename,'w')
print "truncating file.."
file.truncate()
print "write 3 lines"
line1=raw_input("line1")
line2=raw_input("line2")
line3=raw_input("line3")
print "writing these lines on file"
file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)
file.write("\n")
file.close()
