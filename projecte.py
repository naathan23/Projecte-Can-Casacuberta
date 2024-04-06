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

def mostrar_llibre(nom_llibre):
    try:
        with open("Llibres.txt", "r") as file:
            for line in file:
                llibre_info = line.strip().split(",")
                if llibre_info[0] == nom_llibre:
                    print("Informació del llibre:")
                    print("Títol:", llibre_info[0])
                    print("Autor:", llibre_info[1])
                    print("Gènere:", llibre_info[2])
                    return
            print("El llibre ", nom_llibre, " no és el llibre a la biblioteca.")
    excepte FileNotFoundError:
        print("El llibre no ha estat trobat")
    except Exception as i:
        print("Ha passat un error", e)

def mostrar_llibres():
    try:
        with open("Llibres.txt", "r") as file:
            print("Aquests són tots els llibres que hi ha: ")
            for line in file:
                llibre_info = line.strip().split(",")
                print("Títol:", llibre_info[0])
                print("Autor:", llibre_info[1])
                print("Gènere:", llibre_info[2])
    except Exception as i:
        print("Ha passat un error:", e)

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

def eliminar_llibre():
    fitxer_llibres = "llibres.txt"
    titol = input("Introdueix el títol del llibre que vols eliminar: ")

    try:
        with open(fitxer_llibres, "r") as arxiu:
            llibres = arxiu.readlines()
            
        llibres_actualitzats = []
        eliminat = False
        for linia in llibres:
            parts = linia.strip().split("|")
            if len(parts) >= 1 and parts[0] == titol:
                eliminat = True
                print(f"El llibre '{titol}' s'ha eliminat del fitxer.")
            else:
                llibres_actualitzats.append(linia)
        if not eliminat:
            print(f"No s'ha trobat cap llibre amb el títol '{titol}'.")
        with open(fitxer_llibres, "w") as arxiu:
            arxiu.writelines(llibres_actualitzats)
    except FileNotFoundError:
        print("L'arxiu no existeix o no es pot llegir. Torna-ho a intentar.")

def editar_llibres():
    fitxer_llibres = "llibres.txt"
    titol = input("Introdueix el títol del llibre a editar: ")
    try:
        with open(fitxer_llibres, 'r') as arxiu:
            llibres=arxiu.readlines()
            trobat=False
            for i,linia in enumerate (llibres):
                parts=linia.strip().split("|")
                if len(parts)>=1 and parts[0]==titol:
                    print(f"S'ha trobat el llibre {titol}")
                    camp_a_editar=input(f"Escriu el camp a editar de {titol} (titol/autor/any de publicacio/genere):")
                    if camp_a_editar=="titol":
                        nou_titol=input("Introdueix el nou títol del llibre: ")
                        parts[0]=nou_titol
                    elif camp_a_editar=="autor":
                        nou_autor=input("Introdueix el nou autor del llibre: ")
                        parts[1]=nou_autor
                    elif camp_a_editar=="any de publicacio":
                        nou_any=input("Introdueix l'any de publicació: ")
                        parts[2]=nou_any
                    elif camp_a_editar=="genere":
                        nou_genere=input("Introdueix el nou gènere: ")
                        parts[3]=nou_genere
                    llibres[i] = "|".join(parts) + "\n"
                    trobat = True
                    break
            if not trobat:
                print(f"No s'ha trobat cap llibre amb el títol {titol}")
                return
        with open(fitxer_llibres, "w") as arxiu:
            arxiu.writelines(llibres)
            print(f"El llibre {titol} ha estat actualitzat amb èxit!")
    except FileNotFoundError:
        print(f"L'arxiu {fitxer_llibres} no existeix.")
        return

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

