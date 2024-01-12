from histoire import *
from dialogue import *
from scene import *
from personnages import *
from utils import *
from environnement import *
from objet import *


# Create the characters
bob = Perso("", "Bob", {}, [])

# Create the scenes
dialogue2 = Dialog("ça va ?", bob)
dialogue3 = Dialog("Au revoir", bob)

# Create the choices
choice1 = Choice("Bonjour", bob, [["Bonjour", dialogue2], ["Au revoir", dialogue3]])


# Create the dialogues
dialogue1 = Dialog("Bonjour", bob, choice1)


# Create the scenes
scene1 = Scene("Scene 1", "C'est la scene 1", None, [dialogue1])

# Create the history
histoire = History("Histoire", scene1)