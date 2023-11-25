class Dialog:
    def __init__(self, scene, text, personnage, nextDialogue=None):
        self.text = text
        self.scene = scene
        self.personnage = personnage
        self.nextDialogue = nextDialogue

    def afficher(self):
        print(self.personnage + " : " + self.text)
        if self.nextDialogue != None:
            self.nextDialogue.afficher()
        else:
            self.scene.nextScene.afficher()
            
class Choice:
    def __init__(self, text, personnage, options):
        self.text = text
        self.personnage = personnage
        self.options = options
        #self.options = [[Texte, nextScene], [Texte, nextScene], [Texte, nextScene]]

    def afficher(self):
        print(self.personnage + " : " + self.text + "\n" + "Choisissez une option :")
        i = 1
        for option in self.options:
            print("\n" + str(i) + ". " + option[0])
            i += 1
        choix = int(input("\nVotre choix : "))
        self.options[choix - 1][1].afficher()

