def litros_a_galones(litros):
    return litros * 0.264172

def galones_a_litros(galones):
    return galones * 3.78541

def litros_a_onzas_fluidas(litros):
    return litros * 33.814

def onzas_fluidas_a_litros(onzas_fluidas):
    return onzas_fluidas * 0.0295735

def main():
    print("Convertidor de volumen")
    print("1. Litros a galones")
    print("2. Galones a litros")
    print("3. Litros a onzas fluidas")
    print("4. Onzas fluidas a litros")
    opcion = input("Ingrese la opción deseada: ")
    if opcion == "1":
        litros = float(input("Ingrese la cantidad de litros: "))
        galones = litros_a_galones(litros)
        print(f"{litros} litros son {galones} galones")
    elif opcion == "2":
        galones = float(input("Ingrese la cantidad de galones: "))
        litros = galones_a_litros(galones)
        print(f"{galones} galones son {litros} litros")
    elif opcion == "3":
        litros = float(input("Ingrese la cantidad de litros: "))
        onzas_fluidas = litros_a_onzas_fluidas(litros)
        print(f"{litros} litros son {onzas_fluidas} onzas fluidas")
    elif opcion == "4":
        onzas_fluidas = float(input("Ingrese la cantidad de onzas fluidas: "))
        litros = onzas_fluidas_a_litros(onzas_fluidas)
        print(f"{onzas_fluidas} onzas fluidas son {litros} litros")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()