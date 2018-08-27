from sys import argv
script, input_file= argv
#below we define a function which print whole file
def print_all(f):
#it read the file f
    print f.read()
#new function is created rewind
def rewind(f):
    #it will take the rowhead to begining
    f.seek(0)

#new function is created which will print line by line
def print_a_line(line_count,f):
    #in this readline will return string until it do not encounter space(/n)
    print line_count, f.readline()
#it will open the input_file file
current_file=open(input_file)
#print
print "first lets us print the whole file:\n"
#call the function print_all
print_all(current_file)

print "now lets rewind"
#call rewind function
rewind(current_file)

print "now lets print 3 files"

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)
