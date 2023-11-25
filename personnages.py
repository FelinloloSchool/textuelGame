class Perso:
    def __init__(self, nom, prenom, relations, inventaire):
        self.nom = nom
        self.prenom = prenom
        self.relations = relations
        self.inventaire = inventaire

    def __str__(self):
        return self.nom + " " + self.prenom
    
    def __repr__(self):
        return "Perso" + self.nom + self.prenom + self.relations
    
