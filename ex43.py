class Map(object):
	
	def __init__(self, start_scene):
		pass
	
	def next_scene(self, scene_name):
		pass
		
	def opening_scene(self):
		pass
		
class Engine(object):

	def __init__(self, scene_map):
		pass
	
	def play(self):
		pass
		
class Scene(object):

	def enter(self):
		pass

class Death(scene):
	
	def enter(self):
		pass

class CentralCorridor(Scene):
	
	def enter(self):
		pass
		
class LaserWeponArmory(Scene):
	
	def enter(self):
		pass

class TheBridge(Scene):
	
	def enter(self):
		pass
		
class EscapePod(Scene):
	
	def enter(self):
		pass
				
a_map = Map('centra_corridor')
a_game = Engine(a-map)
a_game = play()