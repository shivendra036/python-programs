from sys import argv

script, filename = argv

txt = open(filename)

print "Here's is your file %r:" % filename
print txt.read()

print "type the file name again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
