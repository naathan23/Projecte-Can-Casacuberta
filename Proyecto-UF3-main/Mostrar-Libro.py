def mostrar_libro(nombre_libro):
    try:
        with open("Llibres.txt", "r") as file:
            for line in file:
                libro_info = line.strip().split(",")
                if libro_info[0] == nombre_libro:
                    print("Información del libro:")
                    print("Título:", libro_info[0])
                    print("Autor:", libro_info[1])
                    print("Género:", libro_info[2])
                    return
            print("El libro ", nombre_libro, " no esta el libro en la biblioteca.")
    except FileNotFoundError:
        print("El libro no ha sido encontrado")
    except Exception as e:
        print("Ha ocurrido un error", e)
