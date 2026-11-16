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
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom    # cree une variable d'instance nom pour chaque objet de la classe Personne
        self.age = age     # cree une variable d'instance age pour chaque objet de la classe Personne
        if nom == "":
            self.DemanderNom()
        print("Constructeur : " + nom )
        
    def se_presenter(self):
        if self.nom == "":
            self.DemanderNom()
        if self.age >0:
            print(f"Bonjour, je m'appelle  {self.nom} et j'ai {self.age} ans.")
        else:
            print(f"Bonjour, je m'appelle  {self.nom}")
        if self.EstMajeur():
            print("Je suis majeur.")
        else:
            print("Je suis mineur.")
        
    def EstMajeur(self):
        return self.age >= 18

    def DemanderNom(self):
        self.nom = input("Quel est votre nom ?")
    
# --------Utilisation de la classe Personne------------
personne1 = Personne("Alice", 30) #je crée un objet personne1 de type Personne
personne2 = Personne("Bob", 15) #je crée un objet personne2 de type Personne
personne3 = Personne()
personne4 = Personne(a=20)

personne1.se_presenter() #je demande à l'objet personne1 d'exécuter la méthode se_presenter
personne2.se_presenter() #je demande à l'objet personne2 d'exécuter la méthode se_presenter
personne3.se_presenter() #je demande à l'objet personne3 d'exécuter la méthode se_presenter
personne4.se_presenter() #je demande à l'objet personne4 d'exécuter la méthode se_presenter

#personne2.EstMajeur() #je demande à l'objet personne2 d'exécuter la méthode EstMajeur











#-----------------------------------------------------------------
""" 
def afficher_informations_utilisateur(nom, age):
    print(f"La personne s'appelle {nom} et a {age} ans.")


nom= "Alexis"
age= 30
afficher_informations_utilisateur(nom, age) """