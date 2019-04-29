from sys import exit

def fatality(why):
	print why, "He goes home after you both eat dinner, you hear that you lost your job and are later exhiled in public."
	exit(0)

def unemployment(why):
	print why, "You don't get the job and never hear from Hugo again. Back to square one."
	exit(0)

def win():
	print "Congratulations, you get the job!"
	exit(0)

def bill_test():
	print "You finish your food and Hugo calls for the bill to come to the table. The bill is $190."
	print "The waitress comes with a credit card machine. What do you do?"
	print "1. Let him pay and thank him in front of the waitress"
	print "2. Pay for the meal before he has the chance"
	bill_pay = raw_input("> ")
	if bill_pay == "1":
		win()
	elif bill_pay == "2":
		fatality("You make Hugo feel small by trying to outshine him in front of the waitress.")
	else:
		print "This isn't an option. Try again."
		bill_test()

def job_test():
	print "Hugo asks you why you want the promotion."
	print "Which approach do you take in your explanation?"
	print "1. Focus on why you would benefit from the job"
	print "2. Focus on why he would benefit from your promotion"
	job_question = raw_input("> ")
	if job_question == "1":
		unemployment("You bore Hugo with details about which he does not care.")
	elif job_question == "2":
		bill_test()
	else:
		print "This isn't an option. Try again."
		job_test()

def joke_test():
	print "Whilst eating your food, Hugo tells a joke and looks to you for his response."
	print "How do you react?"
	print "1. Don't laugh, shake your head and mock his sense of humour"
	print "2. Laugh"
	print "3. Chuckle"
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
	print "Hugo comments positively on your clothes."
	print "How do you react?"
	print "1. Tell him you got it at a charity shop and that you appreciate his comment."
	print "2. Briefly say where you got it and tell him you love his suit."
	print "3. Tell him how expensive the shirt was and make a joke about his clothes looking cheap for Hugo Boss."
	clothes_reaction = raw_input("> ")
	if clothes_reaction == "1" or clothes_reaction == "2":
		print "Hugo appreciates your reaction."
		joke_test()
	elif clothes_reaction == "3":
		fatality("You see a twitch in Hugo's eyebrow.")
	else:
		print "That's not an option."
		clothes_test()

def start():
	print "You sit down with Hugo Boss for dinner to discuss a possibility of you moving from JD and"
	print "being promoted at his company."
	clothes_test()

start()
	
	