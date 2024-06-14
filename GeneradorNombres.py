def obtener_nombre():
    superheroe = input("¿Cuál es tu superhéroe favorito? ")
    color = input("¿Cuál es tu color favorito? ")
    animal = input("¿Cuál es tu animal favorito? ")
    ciudad = input("¿Cuál es tu ciudad favorita? ")

    print("\nSelecciona el formato del nombre:")
    print("1. Superhéroe + Color")
    print("2. Superhéroe + Animal")
    print("3. Ciudad + Color")
    print("4. Ciudad + Animal")
    print("5. Superhéroe + Color + Animal + Ciudad")
    print("6. Color + Superhéroe + Ciudad")
    print("7. Animal + Ciudad + Color")
    print("8. Ciudad + Superhéroe + Animal + Color")
    opcion = input("Elige una opción (1-8): ")

    if opcion == "1":
        nombre = f"{superheroe} {color}"
    elif opcion == "2":
        nombre = f"{superheroe} {animal}"
    elif opcion == "3":
        nombre = f"{ciudad} {color}"
    elif opcion == "4":
        nombre = f"{ciudad} {animal}"
    elif opcion == "5":
        nombre = f"{superheroe} {color} {animal} {ciudad}"
    elif opcion == "6":
        nombre = f"{color} {superheroe} {ciudad}"
    elif opcion == "7":
        nombre = f"{animal} {ciudad} {color}"
    elif opcion == "8":
        nombre = f"{ciudad} {superheroe} {animal} {color}"
    else:
        print("Opción no válida. Usando formato por defecto.")
        nombre = f"{superheroe} {color}"

    return nombre

def main():
    nombre = obtener_nombre()
    print("\n--- Generador de Nombres ---")
    print(f"El nombre es: \"{nombre}\"")

if __name__ == "__main__":
    main()
