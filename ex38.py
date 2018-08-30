ten_things= "Apple Oranges Crows Telephone Light Sugar"

print "Wait there is not 10 things in that list,let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Days","Night","Songs","Frisbee","Corn","Banana","Girl","boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "adding:",next_one
    stuff.append(next_one)
    print "There's %d items now." %len(stuff)

print "there we go:",more_stuff
print "let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
