from sys import argv

script, goalone, goaltwo, goalthree = argv

print "You are not achieving the following goals: %s, %s, %s" % (goalone, goaltwo, goalthree)
# goals
print "Let's deal with the %s goal first." % (goalone)
print "What is the first step to achieving %s?" % (goalone)
first_step_one = raw_input("> ")
print "How motivated do you feel on a scale from 1-10 for this goal?" 
motivation_one = raw_input("> ")

print """You are %d /10 motivated for %s. But this is irrelevant. What matters is that you are trying. Notice that all around you, 
from friends such as Leon and Max, to brothers such as Jawad and Jihad, to your own parents, you will encounter
negativity. You must constantly fill yourself with positivity and reflect negativity off of you as if it came from within you.
Stand up and %r.""" % (motivation_one, goalone, first_step_one)

print "Let's deal with the %s goal next." % (goaltwo)
print "What is the first step to achieving %s?" % (goalone)
first_step_two = raw_input("> ")
print "How motivated do you feel on a scale from 1-10 for this goal?" 
motivation_two = raw_input("> ")

print """You are %d /10 motivated for %s. But this is irrelevant. What matters is that you are trying. Notice that all around you, 
from friends such as Leon and Max, to brothers such as Jawad and Jihad, to your own parents, you will encounter
negativity. You must constantly fill yourself with positivity and reflect negativity off of you as if it came from within you.
Stand up and %r.""" % (motivation_two, goaltwo, first_step_two)

print "Let's deal with the %s goal lastly." % (goalthree)
print "What is the first step to achieving %s?" % (goalthree)
first_step_three = raw_input("> ")
print "How motivated do you feel on a scale from 1-10 for this goal?" 
motivation_three = raw_input("> ")

print """You are %d /10 motivated for %s. But this is irrelevant. What matters is that you are trying. Notice that all around you, 
from friends such as Leon and Max, to brothers such as Jawad and Jihad, to your own parents, you will encounter
negativity. You must constantly fill yourself with positivity and reflect negativity off of you as if it came from within you.
Stand up and %r.""" % (motivation_three, goalthree, first_step_three)




