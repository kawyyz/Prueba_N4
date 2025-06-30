def valida_num(mensaje:str=""):
    while True:
        try:
            numero = int(input(mensaje))
            if numero <= 0:
                print("Error, el numero debe ser positivo.")
                continue
        except ValueError:
            print("Error, solo se permiten numeros enteros.")
            continue
        return numero
def valida_txt(mensaje:str=""):
    while True:
        texto = input(mensaje).strip()
        if not texto:
            print("Error, el texto no puede estar vacio.")
            continue
        if any(x in "0123456789" for x in texto):
            print("Error, el texto no puede tener numeros.")
            continue
        return texto
def valida_codigo(mensaje:str=""):
    while True:
        codigo = input(mensaje)
        if len(codigo) > 6 and codigo.isalnum():
            if any(x in "0123456789" for x in codigo):
                if any(x in "ABCDEFGHIJKLMNÑOPQRTSUVWXYZ" for x in codigo):
                    return codigo
                else:
                    print("Error, el codigo debe tener mas de 6 caracteres alfanumericos.")
                continue
            else:
                print("Error, el codigo debe tener mas de 6 caracteres alfanumericos.")
            continue
        else:
            print("Error, el codigo debe tener mas de 6 caracteres alfanumericos.")
            continue

registro = {
    "entradas":[

    ]
}

stock_concepcion = 500
stock_ptealto = 1300
stock_mllebaron = 100
stock_mllevergara = 50

while True:
    print("TOTEM AUTOSERVICIO GIRA ROOCK AND CHILE IN CHILE")
    print("[1]- Comprar entrada a 'los Fortificados' en Concepcion")
    print("[2]- Comprar entrada a 'los Fortificados' en Puente Alto")
    print("[3]- Comprar entrada a 'los Fortificados' en Muelle Baron Valparaiso")
    print("[4]- Comprar entrada a 'los Fortificados' en Muelle Vergara Viña del mar")
    print("[5]- Salir")

    opcion = valida_num("Ingrese la sede donde desea comprar.")

    if opcion == 1:
        while True:
            nombre = valida_txt("Ingrese su nombre: ")
            if nombre in registro["entradas"]:
                print("El nombre no debe estar repetido.")
                continue
            else:
                break
        venta = {
           "nombre":nombre
        }
        registro["entradas"].append(venta)
        codigo = valida_codigo("Ingrese el codigo de su compra.")
        stock_concepcion -= 1
        print(f"Entrada registrada! Stock restante: {stock_concepcion}")
    elif opcion == 2:
        while True:
            nombre = valida_txt("Ingrese su nombre: ")
            if nombre in registro["entradas"]:
                print("El nombre no debe estar repetido.")
                continue
            else:
                break
        venta = {
           "nombre":nombre
        }
        registro["entradas"].append(venta)
        while True:
            entradas = valida_num("Ingrese el numero de entradas.")
            if entradas > 3:
                print("Error, solo se permiten entre 1 y 3 entradas por persona")
                continue
            else:
                break
        stock_ptealto -= entradas
        print(f"Entrada registrada! Stock restante: {stock_ptealto}")
    elif opcion == 3:
        while True:
            nombre = valida_txt("Ingrese su nombre: ")
            if nombre in registro["entradas"]:
                print("El nombre no debe estar repetido.")
                continue
            else:
                break
        venta = {
           "nombre":nombre
        }
        registro["entradas"].append(venta)
        print("Tipo de entrada asignado: G")
        stock_mllebaron -= 1
        print(f"Entrada registrada! Stock restante: {stock_mllebaron}")
    elif opcion == 4:
        while True:
            nombre = valida_txt("Ingrese su nombre: ")
            if nombre in registro["entradas"]:
                print("El nombre no debe estar repetido.")
                continue
            else:
                break
        venta = {
           "nombre":nombre
        }
        registro["entradas"].append(venta)
        while True:
            entrada = valida_txt("Ingrese el tipo de entrada 'Sun' (Sunset) o 'Ni' (Night).")
            if entrada == "Sun" or entrada == "sun" or entrada == "Ni" or entrada == "ni":
                tipo_entrada = entrada
                break
            else:
                print("Error, solo se permite 'Sun' o 'Ni'.")
                continue
        stock_mllevergara -= 1
        print(f"Entrada registrada! Stock restante: {stock_mllevergara}")
    elif opcion == 5:
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opcion valida!")
        continue