def mostrar_todos_libros():
    try:
        with open("Llibres.txt", "r") as file:
            print("Estos son todas los libros que hay: ")
            for line in file:
                libro_info = line.strip().split(",")
                print("Título:", libro_info[0])
                print("Autor:", libro_info[1])
                print("Género:", libro_info[2])
    except Exception as e:
        print("Ha ocurrido un error:", e)
