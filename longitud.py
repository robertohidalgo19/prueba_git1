def metros_a_pulgadas(metros):
    return metros * 39.37

def pulgadas_a_pies(pulgadas):
    return pulgadas * 0.0833333

def main():
    print("Convertidor de longitud")
    print("1. Metros a pulgadas")
    print("2. Pulgadas a pies")
    opcion = input("Ingrese la opción deseada: ")
    if opcion == "1":
        metros = float(input("Ingrese la cantidad de metros: "))
        pulgadas = metros_a_pulgadas(metros)
        print(f"{metros} metros son {pulgadas} pulgadas")
    elif opcion == "2":
        pulgadas = float(input("Ingrese la cantidad de pulgadas: "))
        pies = pulgadas_a_pies(pulgadas)
        print(f"{pulgadas} pulgadas son {pies} pies")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()