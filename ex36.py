print "ENTER YOUR NAME"
name=raw_input("\n>")
print "WELCOME MAJOR",name,"YOU ARE THE AN OFFICER OF INDIAN ARMED FORCE.\n\nYOU ARE CURRENTLY SERVING IN 1/11 RASHTRIYA RIFLES AND POSTED IN KASHMIR."
print "\n"
print"""
Your Commander Assign You a Task of Eliminating The
Terrorist Hidden in a House near Poonch in a Village.
Make a Company, Prepare a Plan and Proceed For Mission
at 2100 hrs.Right Now it's 1800 hrs.
GOOD LUCK.
"""


def company():
    print "Formation of a company."
    print "You  had following options for company formation"
    print"""
    1.20 Soldier, 5 JCO
    2.21 Soldier, 4 JCO
    3.15 Soldier, 5 JCO
    4.18 Soldier, 4 JCO
    """
    i=int(raw_input())
    if i==1:
        print "you have form company of 20 Soldiers and 5 JCO.Good Job."
        s=20
        j=5
    elif i==2:
        print "you have form company of 21 Soldiers and 4 JCO.Good Job."
        s=21
        j=4
    elif i==3:
        print "you have form company of 15 Soldiers and 5 JCO.Good Job."
        s=15
        j=5
    elif i==4:
        print "you have form company of 18 Soldiers and 4 JCO.Good Job."
        s=18
        j=4
    else:
        print "Please enter a valid option."
        company()
    print "\n\nFINALLY YOU FORMED YOUR TEAM AND REACH TO THE SITE."
    print "HOW WILL YOU PROCEED."
    print "HINT----DEVIDE YOUR TEAM INTO SMALL GROUP!!"
    print "HOW YOU WILL DIVIDE MENTION SOLDIER AND JCO IN A SINGLE GROUP HERE -"
    s1=int(raw_input("SOLDIER="))
    j1=int(raw_input("JCO="))

    if s%s1==0 and j%j1==0 and s>s1 and j>j1 :
        print "\n%d GROUP FORMED" %((s+j)/(s1+j1))
    elif s%s1!=0 and j%j1!=0 and s>s1 and j>j1:
        a=(s-s%s1)/s1
        b=(j-j%j1)/j1
        print "%d GROUP FORMED WHILE SOLDIER=%d AND JCO=%d WILL BE BEHIND YOU." %((s+j)/(a+b),a,b)


company()
