class Dialog:
    def __init__(self, text:str, personnage, nextDialogue=None):
        self.text = text
        self.personnage = personnage
        self.nextDialogue = nextDialogue

    def afficher(self):
        print(self.personnage.prenom + " : " + self.text)
        if self.nextDialogue != None:
            self.nextDialogue.afficher()

class Choice:
    def __init__(self, text, personnage, options):
        """
        Initializes a Choice object with the given text, character, and options.

        Args:
            text (str): The text of the choice.
            personnage (personnage): The character speaking the choice.
            options (list): A list of options available for the choice. Each option is a list containing the text of the option and the next dialogue or scene.
        """
        self.text = text
        self.personnage = personnage
        self.options = options
        #self.options = [[Texte, nextDialogue], [Texte, nextScene], [Texte, nextScene]]

    def afficher(self):
        """
        Displays the choice and prompts the user to select an option.
        """
        print(self.personnage.prenom + " : " + self.text + "\n" + "Choisissez une option :")
        i = 1
        for option in self.options:
            print("\n" + str(i) + ". " + option[0])
            i += 1
        choix = int(input("\nVotre choix : "))
        self.options[choix - 1][1].afficher()