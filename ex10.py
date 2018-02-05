from sys import argv

script, user_name = argv
prompt = '> '

print "hi %s, I'm the %s script." %(user_name, script)
print "i'd like to ask you a few questions..."
print "do you like me %s?" %(user_name)

likes = raw_input(prompt)

print "where do you live, %s?" %(user_name)
lives = raw_input(prompt)

print "what kinda computer do you've?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you've a %r computer. Nice.
"""%(likes, lives, computer)