
compras = []

def agregar_compra():
    compras.append(int(input("Ingrese el monto de la compra: ")))
    print(f"\nLa compra {compras[len(compras)-1]} se ha agregado correctamente\n")

def mostrar_compras():
    if len(compras) == 0:
        print("\nLa lista de compras está vacía\n")
    else:
        print("\nLista de compras:")
        for i in range(len(compras)):
            print(f"Compra: {i+1} - Monto: {compras[i]}")

def mostrar_total():
    if len(compras) == 0:
        print("\nLa lista de compras está vacía\n")
    else:
        total_gastado = 0
        for i in range(len(compras)):
            total_gastado += compras[i]
        print(f"\nTotal gastado: ${total_gastado:.2f}")

def main():
    v_opciones = [1, 2, 3, 4]
    while True:
        print("\nMenú:\n"
              "1. Agregar compra\n"
              "2. Mostrar compras\n"
              "3. Mostrar total gastado\n"
              "4. Salir\n")

        v_seleccion = int(input("Seleccione una opción: "))

        if v_seleccion == v_opciones[0]:
            agregar_compra()
        elif v_seleccion == v_opciones[1]:
            mostrar_compras()
        elif v_seleccion == v_opciones[2]:
            mostrar_total()
        elif v_seleccion == v_opciones[3]:
            print("\n¡Hasta luego!")
            exit()
        else:
            print("Debe seleccionar una de las 4 opciones")

main()