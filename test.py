# Classe parent
class EtreVivant:
    def respirer(self):
        print("Je respire.")

    def dormir(self):
        print("Je dors.")


# Classe Personne
class Personne(EtreVivant):
    def parler(self):
        print("Bonjour, je parle.")

    def manger(self):
        print("Je mange.")


# Classe Chat
class Chat(EtreVivant):
    def miauler(self):
        print("Miaou !")

    def chasser(self):
        print("Je chasse une souris.")


# Création des objets
personne = Personne()
chat = Chat()

personne.respirer()
personne.parler()

chat.respirer()
chat.miauler()