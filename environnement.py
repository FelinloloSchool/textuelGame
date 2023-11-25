class Lieu:
    def __init__(self, nom, description, voisins):
        self.nom = nom
        self.description = description
        self.voisins = voisins
    
    def __str__(self):
        return self.nom + " : " + self.description
    
    def __repr__(self):
        return "Lieu" + self.nom + self.description + self.voisins
    
    