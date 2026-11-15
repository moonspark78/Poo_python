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
    def __init__(self, nom: str, age: int):
        self.nom = nom    # cree une variable d'instance nom pour chaque objet de la classe Personne
        self.age = age     # cree une variable d'instance age pour chaque objet de la classe Personne
        print("Constructeur : " + nom )
        
    def se_presenter(self):
        print(f"Bonjour, je m'appelle  {self.nom} et j'ai {self.age} ans.")
        
    def EstMajeur(self):
        if self.age >= 18:
            print(f"{self.nom} est majeur.")
        else:
            print(f"{self.nom} est mineur.")

# --------Utilisation de la classe Personne------------
personne1 = Personne("Alice", 30) #je crée un objet personne1 de type Personne
personne2 = Personne("Bob", 15) #je crée un objet personne2 de type Personne

personne1.se_presenter() #je demande à l'objet personne1 d'exécuter la méthode se_presenter
personne2.se_presenter() #je demande à l'objet personne2 d'exécuter la méthode se_presenter














#-----------------------------------------------------------------
""" 
def afficher_informations_utilisateur(nom, age):
    print(f"La personne s'appelle {nom} et a {age} ans.")


nom= "Alexis"
age= 30
afficher_informations_utilisateur(nom, age) """