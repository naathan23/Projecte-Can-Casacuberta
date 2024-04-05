import hashlib

def carregar_usuaris(arxiu):
    usuaris={}
    try:    
        with open("usuaris.txt", "r") as arxiu:
            for linia in arxiu:
                parts=linia.strip().split("|")
                if len(parts)==2:
                    usuari,contrasenya_xifrada=parts
                    usuaris[usuari]=contrasenya_xifrada
    except FileNotFoundError:
            print("L'arxiu no existeix, torna-ho a intentar")
    return usuaris
        
def verificar_usuaris(usuari,usuaris,contrasenya):
    if usuari in usuaris:
        hash_md5=hashlib.md5(contrasenya.encode()).hexdigest()
        return usuaris[usuari]==hash_md5
    return False

def inici_sessio():
    intents=0
    max_intents=3
    arxiu="usuaris.txt"
    usuaris=carregar_usuaris(arxiu)
    usuari_iniciat=False

    while intents<max_intents:
        if not usuari_iniciat: 
            usuari=input("Usuari: ")
            contrasenya=input("Contrasenya: ")
            if verificar_usuaris(usuari,usuaris,contrasenya):
                print(f"Inici de sessió exitós, benvingut {usuari}!\n")
                usuari_iniciat=True
                return True
            else:
                intents+=1
                print(f"Usuari o contrasenya incorrectes. Et resten {max_intents-intents} intents")
    if intents>=max_intents:
        print("Has arribat al límit d'intents, el programa es tancarà.")

def afegir_llibres():
    fitxer_llibres="llibres.txt"
    nom=input("Introdueix el títol del llibre: ")
    autor=input("Introdueix l'autor del llibre: ")
    any_publicacio=input("Introdueix l'any de publicacio del llibre: ")
    genere=input("Introdueix el gènere del llibre: ")
    isbn=input("Introdueix l'ISBN del llibre: ")
    info_llibre = f"\n{nom}|{autor}|{any_publicacio}|{genere}|{isbn}"
    try:
        with open(fitxer_llibres, "a") as arxiu:
            if nom in open(fitxer_llibres).read():
                print(f"El llibre {nom} ja existeix, torna-ho a provar.")
            else:
                arxiu.write(info_llibre)
                print(f"El llibre {nom} ha estat afegit amb èxit.")
    except FileNotFoundError:
        print(f"L'arxiu {fitxer_llibres} no existeix, si us plau crea l'arxiu abans d'afegir llibres.")
    
def Menu():
    print("*************************************")
    print("     Biblioteca Can Casacuberta      ")
    print("*************************************")
    print("Escull una opció a fer amb els llibres:\n")
    print("1. Mostrar un llibre\n")
    print("2. Mostrar tots els llibres\n")
    print("3. Afegir un llibre\n")
    print("4. Eliminar un llibre\n")
    print("5. Editar un llibre\n")

