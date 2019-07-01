from sys import exit
import math
import random


def fatality(why):
	print why, "He goes home after you both eat dinner, you hear that you lost your job and are later exhiled in public."
	exit(0)

def death_by(what):
	print what
	exit(0)

def unemployment(why):
	print why, "You don't get the job and never hear from Hugo again. Back to square one."
	exit(0)

def win():
	print "Congratulations, you get the job!"
	exit(0)

def bill_test():
	print """You finish your food and Hugo calls for the bill to come to the table. 
The bill is $30 (the 2019 equivalent is $544).
The waitress comes with a credit card machine. What do you do?
1. Let him pay and thank him in front of the waitress
2. Pay for the meal before he has the chance on your credit card"""
	bill_pay = raw_input("> ")
	
	if bill_pay == "1":
		win()
	elif bill_pay == "2":
		fatality("You make Hugo feel small by trying to outshine him in front of the waitress.")
	else:
		print "This isn't an option. Try again."
		bill_test()

def car_talk():
	print "You approach Hugo's car."

	print """Two men walk by with partly concealed faces. From the way they are standing,
one of them with a hand in their jacket pocket, it seems he might have some kind of a weapon.
They approach you and Hugo.\n
\"Nice car. Want to hand over them keys?\", one of them says.
Hugo says \"No way.\". The man pulls out a gun and points it at Hugo. 
The man says \"Now!\" and points the gun at Hugo's head. 
The other man moves closer. What do you do?\n"""

	print """1. Punch the man with the weapon in the face.
2. Try to perform Brazillian Jiu Jitsu on the man with the weapon.
3. Surrender, let them take Hugo's keys and offer to take Hugo home."""

	
	robbery_reaction = raw_input("> ")
	rng_1 = random.randint(1, 100)

	if robbery_reaction == "1" and rng_1 > 90:
		print """You manage to hit the man hard enough to make him unconscious.
The man drops to the ground. With a swiftness you pick up his gun and point it 
at the other man."""
		print "You and Hugo get away safely. Hugo feels he owes you greatly."
		win()

	elif robbery_reaction == "1" and rng_1 <= 90:
		death_by("You don't hit him hard enough, he turns and shoots you with a gun.")

	elif robbery_reaction == "2" and rng_1 > 95:
		print """You put the man in a kind of choke hold, disarming him of his weapon.
Hugo picks up the weapon, points it at one of the men and you both manage to get away 
in Hugo's car safely."""
		print "Hugo feels he owes you greatly."
		win()

	elif robbery_reaction == "2" and rng_1 <= 95:
		death_by("""Your years of BJJ training ends in failure as you get shot in the 
leg during a grapple.""")

	elif robbery_reaction == "3":
		print "Hugo joins you in your car. He thanks you for taking you home."
		win()



def bankbreak():
	print """Hugo explains more. As he is talking, you see that he is becoming excited, glowing from his success.
He explains that success requires an incredible amount of patience, dedication, faith and passion. 
You can react at any level of enthusiasm to his story, 1 being enviously unenthusiastic and 10 being inspired and very enthusiastic.
How would you like to react?"""
	
	exicted_number = int(raw_input("> "))
	
	if exicted_number >= 4:
		print "Hugo likes your response and attitude."
		bill_test()
	elif exicted_number < 4:
		unemployment("Hugo appears to feel bad for you.")
	else:
		print "This isn't an option. Try again."
		bankbreak()

def deep_bar_talk():
	print """You buy a %r and sit down with Hugo.
Hugo asks you what you would like advice on.
Choose your problem.
1. Your relationship problems
2. Your confusion about ambitions and goals
3. Your existential dread
4. Your bad habits""" % (which_drink)
	bar_problems = raw_input("> ")
	
	if bar_problems == "1" or bar_problems == "3" or bar_problems == "4":
		unemployment("You and Hugo seem to have a good time and conversation.")
	elif bar_problems == "2":
		print "Hugo's eyes light up."
		print "Hugo says he can tell you are ambitious and you should be confused."
		print "\"I'll offer you one piece of advice, %r.\" Hugo says, before taking a sip of his drink." % (name)
		print """\"Keep asking questions like that. I can't solve that for you because I am not you. 
Just keep asking those questions and ponder them seriously.\" Hugo pays for the drinks
and you both leave the bar.""" 
		car_talk()
	else:
		print "That's not an option. Try again."
		bar_talk()


def bar_talk():
	print """You and Hugo arrive at the bar.
Upon walking upto the bar, you see that there is a selection of different drinks on offer.
The menu reads:"""
	
	drinks = ['whiskey', 'beer', 'gin and tonic', 'water', 'vodka', 'rum', 'sambouka']
	for p in drinks: print p
	print "Which drink would you like to buy?"
	global which_drink
	which_drink = raw_input("> ")

	deep_bar_talk()
		
def bar_req():
	print """You ask Hugo about your problems.
Hugo is happy to tell you what to do and how to solve your issues.
Hugo asks if you would like to go out for a drink afterwards at a local bar to talk more.
What do you do?
1. Say yes.
2. Say no because you have work to do tonight."""
	
	guiding_answer = raw_input("> ")
	
	if guiding_answer == "1":
		bar_talk()
	elif guiding_answer == "2":
		next_guiding_answer = "2"
		while next_guiding_answer == "2":
			print "Hugo responds \"Oh, come on! I know a great place just around the corner, all drinks are on me.\""
			print "How do you respond?"
			print "1. Ok."
			print "2. No."
			next_guiding_answer = raw_input("> ")
	else:
		print "That's not an option. Try again."
		bar_req()
		
	if next_guiding_answer == "1":
		bar_talk()
	else:
		print "That's not an option. Try again."
		bar_req()

def hugo_story():
	print """Hugo seems happy with your answer.
Hugo seems like he's about to open up about his past.
\"When I was your age, I employed 30 people to help run my clothing factory and had financial backing.
The situation in Germany was very problematic for us. In last year I filed for bankruptcy.
My creditors didn't want to go forward and it seemed as if I had lost everything.

Even though we had lost everything, I believed in my business and I had a vision for it. 
I wasn't going to just give up. I pleaded and negotiated with my creditors trying to 
get them to give me something to restart my business. I had no money and
I had to move back to living with my dad and sell a lot of my resources. 

My creditors decided to give me six sewing machines. I restarted my business from scratch. This year we're doing 
much better and I've recently been contacted by the government to begin a line of military clothing.\"
What is your method of response?
1. Ask him more about what fascinated you in the story.
2. Revert back to what you were saying after quickly commenting on how delightful his story was.
3. Take this opportunity to ask him for some guidance in your life."""
	
	story_reply = raw_input("> ")
	
	if story_reply == "1":
		print "Hugo tells you more about the story."
		bankbreak()
	elif story_reply == "2":
		unemployment("Hugo doesn't like your selfish and careless attitude.")
	elif story_reply == "3":
		bar_req()

def experience_q():
	print """Hugo likes your answer. He asks you to tell him about yourself.
How do you approach the answer to his question?
1. Be completely honest and humble
2. Bend the truth to suit his needs"""
	experience_a = raw_input("> ")
	
	if experience_a == "1":
		hugo_story()
	elif experience_a == "2":
		unemployment("Hugo becomes unimpressed.")
	else:
		print "This isn't an option. Try again."
		experience_q()

def job_test():
	print """Hugo asks you why you want the promotion.
Which approach do you take in your explanation?
1. Focus on why you would benefit from the promotion
2. Focus on why he would benefit from your promotion"""
	job_question = raw_input("> ")
	
	if job_question == "1":
		unemployment("You bore Hugo with details about which he does not care.")
	elif job_question == "2":
		experience_q()
	else:
		print "This isn't an option. Try again."
		job_test()
	
def joke_test():
	print """Whilst eating your food, Hugo suddenly smiles and looks as if he's about to tell a joke.
\"Do you want to hear a joke about paper?\"
Before you can react, Hugo says \"Never mind, it's tearable.\"
How do you react to this joke?
1. Don't laugh, shake your head and mock his sense of humor
2. Laugh
3. Chuckle"""
	joke_reaction = raw_input("> ")
	
	if joke_reaction == "1":
		fatality("You can see that you offended Hugo with your comment.")
	elif joke_reaction == "2" or joke_reaction == "3":
		print "You and Hugo laugh together. He looks happy."
		job_test()
	else:
		print "That's not an option. Try again."
		joke_test()

def clothes_test():
	print """Hugo comments positively on your clothes.
How do you react?
1. Tell him you got it at a charity shop and that you appreciate his comment.
2. Briefly say where you got it and tell him you love his suit.
3. Tell him how expensive the shirt was and make a joke about his clothes looking cheap."""
	clothes_reaction = raw_input("> ")
	
	if clothes_reaction == "1" or clothes_reaction == "2":
		print "Hugo appreciates your reaction."
		joke_test()
	elif clothes_reaction == "3":
		fatality("You see a twitch in Hugo's eyebrow.")
	else:
		print "That's not an option."
		clothes_test()

def name_q():
	print "What is your name?"
	global name
	name = raw_input("> ")
	print "Good luck, %r." % (name)
	
	clothes_test()

def start():
	print """It is the year 1932. You sit down with Hugo Boss for dinner to discuss a possibility
of you moving from your current company and being promoted at his clothing start-up."""
	name_q()

start()