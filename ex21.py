def add(a,b):
    print "adding %d + %d" %(a,b)
    return a+b
def sub(a,b):
    print "sub %d - %d" %(a,b)
    return a-b
def mul(a,b):
    print "mul %d * %d" %(a,b)
    return a*b
def devide(a,b):
    print "devide %d / %d"
    return a/b
age=add(30,5)
height=sub(78,4)
weight=mul(90,2)
iq=devide(100,2)
print "age=%d,height=%d,weight=%d,iq=%d" %(age,height,weight,iq)
print "here is a puzzle"
what=add(age,sub(height,mul(weight,devide(iq,2))))
print "that becomes", what
