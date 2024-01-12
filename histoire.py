from typing import Any


class History:
    def __init__(self, nom, premiereScene):
        self.nom = nom
        self.premiereScene = premiereScene
        self.sceneActuelle = premiereScene

    def start(self):
        self.sceneActuelle.afficher()
        print("Fin de l'histoire")