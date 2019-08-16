from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		pass
		
class Engine(object):
		
	def __init__(self, scene_map):
		pass
	
	def play(self):
		pass
	
class Death(Scene):

	def enter(self):
		print """You don't make it out alive. The Gothons take you captive
and ensure that you have nothing to do but listen to their jokes until
you starve to death."""
	exit(0)

class CentralCorridor(Scene):

	def Gothon(self, joke):
		print "Gothon hears your joke and dies."

	def enter(self):
		print """As you enter the Central Corridor you notice there is 
a Gothon standing in front of you. He seems to be expecting entertainment
from you."""
		
class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass
		
class EscapePod(Scene):

	def enter(self):
		pass
		

class Map(object):

	def __init__(self, start_scene):
		pass
		
	def next_scene(self, scene_name):
		pass
		
	def opening_scene(self):
		pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

