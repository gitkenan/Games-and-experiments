from sys import exit

def dead(reason):
	print reason, "You disintigrate and wake up on Earth where you are dying. You slowly fade to black."
	exit(0)

print "Welcome to the Afterlife. What is your name?"

name = raw_input("> ")

print """You know you are %s. You died in a tragic accident, which you remember vividly. However,
you don't understand where you are or what you see. The event of your death lead to an intense trip
which lasted what seemed like a few weeks. In these few weeks, you experienced your whole life and more,
an indescribable feeling that you understood the whole universe and your place within it in relation to 
your effect on the world. Right now, you can see nothing but blackness even though you can feel yourself
stood on a warm, soft floor and feel a soft wind. Judging by the sound of the wind, you sense you are in 
an incredibly large open outer-space.
You can't see your body. 
You hear a voice, loud enough to send a vibration through your whole body, say:
\t'Hello %s and welcome to the afterlife. I am God. Walk to the gate'
As God is speaking, you begin to feel a bright light emitting from behind you as you hear him talk
from above, kind of like how you would have imagined on Earth. You begin to see your body is naked but you 
feel warm. The ground infront of you is a very wide and long road which stretches to a giant harp-looking gate. 
What do you want to do?""" % (name, name)
print "1. Walk towards the gate."
print "2. Reply to God."

walkorspeak = raw_input("> ")

if walkorspeak == "1":
	print "The walk to the gate looks like it will take a while. You begin walking and notice that your body feels light."
elif walkorspeak == "2":
	print "What do you want to say to God?"
	print "1. \"Why should I walk to the gate?\""
	print "2. \"No, I don't want to.\""
	print "3. \"Why did you kill me?\""
	print "4. \"Take me back. You can't kill me like that.\""
	
	first_response = raw_input("> ")
	
	if first_response == "1":
		dead("""You hear and feel God take a deep breath in from above. From the sound and speed of his inhale,
			you feel like he thinks you missed the point of the game. After a moment, the soft ground below you 
			begins to sink.""")
else:
	print "You can't do that."

