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

