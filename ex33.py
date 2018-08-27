i=0
numbers=[]
for i in range(0,6):
    print "at the top i is %d" %i
    numbers.append(i)
    i=i+1
    print "numbers now: ",numbers
    print "at the bottom i is %d" %i

print "the numbers:"
for num in numbers:
    print num
