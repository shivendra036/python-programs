from sys import argv

script, user_name = argv
prompt= "> "
print "hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes =raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print"""
alright, so you said %r about liking me.
You live in %r. Not sure what that is.
And you have a %r computer. nice.
""" %(likes, lives, computer)
