def calcular_comision(ventas_totales, porcentaje_comision):
    try:
        ventas_totales = float(ventas_totales)
        porcentaje_comision = float(porcentaje_comision)  # Conversión añadida
        comision = (ventas_totales * porcentaje_comision) / 100
        return "{:.2f}".format(comision)
    except ValueError:
        return None

def calcular_iva(monto, tasa_iva):
    try:
        monto = float(monto)
        tasa_iva = float(tasa_iva)  # Conversión añadida
        iva = (monto * tasa_iva) / 100
        return "{:.2f}".format(iva)
    except ValueError:
        return None

def menu():
    print("\nMenú de opciones:")
    print("1. Calcular comisión")
    print("2. Calcular IVA")
    print("3. Salir")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Por favor, ingresa tu nombre: ")
            ventas_totales = input("Por favor, ingresa el total de tus ventas este mes: ")
            porcentaje_comision = input("Por favor, ingresa el porcentaje de comisión: ")
            comision_formateada = calcular_comision(ventas_totales, porcentaje_comision)

            if comision_formateada is not None:
                print(f"Hola {nombre}, tus comisiones para este mes son: ${comision_formateada}")
            else:
                print("El valor ingresado para las ventas o el porcentaje de comisión no es válido. Por favor, intenta de nuevo.")

        elif opcion == '2':
            monto = input("Por favor, ingresa el monto: ")
            tasa_iva = input("Por favor, ingresa la tasa de IVA: ")
            iva_formateado = calcular_iva(monto, tasa_iva)

            if iva_formateado is not None:
                print(f"El IVA sobre ${monto} a una tasa de {tasa_iva}% es: ${iva_formateado}")
            else:
                print("El valor ingresado para el monto o la tasa de IVA no es válido. Por favor, intenta de nuevo.")

        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

if __name__ == "__main__":
    main()
