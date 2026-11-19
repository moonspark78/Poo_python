def bonjour(nom, age=18, taille=1.75):
    print(f"Bonjour, je m'appelle {nom}, j'ai {age} ans et je mesure {taille} mètre(s).")
    
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

def sub(a, b):
    result = a - b
    print(f"{a} - {b} = {result}")
    return result

bonjour("Jean", 1.80)
print(f"Le resultat de l'addition est : {add(5, 3)}")
print(f"Le resultat de la soustraction est : {sub(5, 3)}")