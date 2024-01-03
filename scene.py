class Scene:
    def __init__(self, name, description, nextScene, dialogues):
        self.name = name
        self.description = description
        self.nextScene = nextScene
        self.dialogues = dialogues
    
    def __str__(self):
        return self.name + " : " + self.description
    
    def __repr__(self):
        return "Scene" + self.name + self.description + self.nextScene + self.dialogues
    
    def afficher(self):
        for dialogue in self.dialogues:
            dialogue.afficher()
        self.nextScene.afficher()
    