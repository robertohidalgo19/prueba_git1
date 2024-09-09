def kilogramos_a_gramos(kilogramos):
    return kilogramos * 1000

def gramos_a_kilogramos(gramos):
    return gramos * 0.001

def kilogramos_a_libras(kilogramos):
    return kilogramos * 2.20462

def libras_a_kilogramos(libras):
    return libras * 0.453592

def main():
    print("Convertidor de peso")
    print("1. Kilogramos a gramos")
    print("2. Gramos a kilogramos")
    print("3. Kilogramos a libras")
    print("4. Libras a kilogramos")
    opcion = input("Ingrese la opción deseada: ")
    if opcion == "1":
        kilogramos = float(input("Ingrese la cantidad de kilogramos: "))
        gramos = kilogramos_a_gramos(kilogramos)
        print(f"{kilogramos} kilogramos son {gramos} gramos")
    elif opcion == "2":
        gramos = float(input("Ingrese la cantidad de gramos: "))
        kilogramos = gramos_a_kilogramos(gramos)
        print(f"{gramos} gramos son {kilogramos} kilogramos")
    elif opcion == "3":
        kilogramos = float(input("Ingrese la cantidad de kilogramos: "))
        libras = kilogramos_a_libras(kilogramos)
        print(f"{kilogramos} kilogramos son {libras} libras")
    elif opcion == "4":
        libras = float(input("Ingrese la cantidad de libras: "))
        kilogramos = libras_a_kilogramos(libras)
        print(f"{libras} libras son {kilogramos} kilogramos")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()