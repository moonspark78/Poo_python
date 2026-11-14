###
# - Différnce programmation impérative / objet
# - Le plus simple possible 
# - Execices,mise en situation,exemples


# Personne (entité -> class)
# Données : nom, age
# Actions : (méthodes)
#          -SePresenter
#          -DemanderAge



# --------Définition de la classe Personne------------
class Personne:
    def __init__(self, nom):
        self.nom = nom
        print("Constructeur : " + nom )
        
    def se_presenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# --------Utilisation de la classe Personne------------
personne1 = Personne("Alice") #je crée un objet personne1 de type Personne
personne2 = Personne("Bob") #je crée un objet personne2 de type Personne

personne1.se_presenter() #je demande à l'objet personne1 d'exécuter la méthode se_presenter












#-----------------------------------------------------------------
""" 
def afficher_informations_utilisateur(nom, age):
    print(f"La personne s'appelle {nom} et a {age} ans.")


nom= "Alexis"
age= 30
afficher_informations_utilisateur(nom, age) """