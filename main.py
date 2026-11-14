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
    pass

# --------Utilisation de la classe Personne------------


def afficher_informations_utilisateur(nom, age):
    print(f"La personne s'appelle {nom} et a {age} ans.")


nom= "Alexis"
age= 30
afficher_informations_utilisateur(nom, age)