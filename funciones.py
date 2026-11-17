def limpiar_terminal() -> None:
    import os
    os.system("cls")

def mostrar_titulo(titulo:str) -> None:
    """Muestra un titulo."""
    print(f"\n- - - - - - - - - - {titulo} - - - - - - - - - -")

def mostrar_opciones() -> None:
    """Muestra las opciones del menú."""
    print("\nOpciones")
    print("\n1 - Cargar ventas")
    print("2 - Mostrar ventas")
    print("3 - Regiones con menos del 5%")
    print("4 - Regiones con menos del 25%")
    print("5 - Regiones con mas de 500 ventas")
    print("6 - Regiones con mas de 3000 ventas")
    print("7 - Regiones por encima del promedio")
    print("8 - Region/es mas compradora/s")
    print("9 - Harcodear vector")
    print("10 - Ordenar regiones por nombre")
    print("11 - Salir")

def validar_numero_entero_positivo(entrada:str) -> bool:
    """Valida que la entrada ingresada sea un numero entero positivo. Devuelve True si lo es, devuelve False si no lo es."""
    entrada = str(entrada)
    for i in entrada:
        if i < "0" or i > "9":
            return False
    return True

def calcular_total_de_lista(lista:list) -> int:
    """Calcula la suma total de numeros en una lista. Devuelve el total."""
    total = 0
    for i in range(len(lista)):
        total += int(lista[i])
    return total

def calcular_porcentajes_de_lista(lista:list) -> list:
    """Calcula los porcentajes en base al total de la lista ingresada. Devuelve una lista con los porcentajes."""
    lista_de_porcentajes = []
    total = calcular_total_de_lista(lista)
    for i in range(len(lista)):
        porcentaje = (int(lista[i]) * 100) / total
        lista_de_porcentajes.append(porcentaje)
    return lista_de_porcentajes

def mostrar_ventas(lista_ventas_de_regiones:list, lista_porcentajes_de_regiones:list):
    """Muestra las ventas ingresadas en una lista."""
    for i in range(len(lista_ventas_de_regiones)):
        print(f"\nREGIÓN N° {i + 1}")
        print(f"Ventas: {lista_ventas_de_regiones[i]}")
        print(f"Porcentaje: {lista_porcentajes_de_regiones[i]}%")
    print(f"\nVENTAS TOTALES: {calcular_total_de_lista(lista_ventas_de_regiones)}")

def validar_existencia_de_elemento_menor_en_lista(lista:list, numero:float) -> bool:
    """Valida si existe un elemento menor a el impuesto en una lista. Devuelve True si existe, devuelve False si no."""
    for i in range(len(lista)):
        if lista[i] < numero:
            return True
    return False

def validar_existencia_de_elemento_mayor_en_lista(lista:list, numero:float) -> bool:
    """Valida si existe un elemento mayor a el impuesto en una lista. Devuelve True si existe, devuelve False si no."""
    for i in range(len(lista)):
        if int(lista[i]) > numero:
            return True
    return False

def mostrar_ventas_menores_a_numero(lista_ventas_de_regiones:list, lista_porcentajes_de_regiones:list, limite:int) -> None:
    """Muestra las ventas que coincidan con el dato ingresado."""
    ventas_acumuladas = 0
    porcentaje_acumulado = 0
    for i in range(len(lista_ventas_de_regiones)):
        if lista_porcentajes_de_regiones[i] < limite:
            print(f"\nREGIÓN N° {i + 1}")
            print(f"Ventas: {lista_ventas_de_regiones[i]}")
            print(f"Porcentaje: {lista_porcentajes_de_regiones[i]}%")
            ventas_acumuladas += int(lista_ventas_de_regiones[i])
            porcentaje_acumulado += float(lista_porcentajes_de_regiones[i])

    print(f"\nVENTAS ACUMULADAS DE LA BUSQUEDA: {ventas_acumuladas}")
    print(f"PORCENTAJE ACUMULADO DE LA BUSQUEDA: {porcentaje_acumulado}%")

def mostrar_ventas_mayores_a_numero(lista_ventas_de_regiones:list, lista_porcentajes_de_regiones:list, limite:int) -> None:
    """Muestra las ventas que coincidan con el dato ingresado."""
    ventas_acumuladas = 0
    regiones_acumuladas = 0
    for i in range(len(lista_ventas_de_regiones)):
        if lista_ventas_de_regiones[i] > limite:
            print(f"\nREGIÓN N° {i + 1}")
            print(f"Ventas: {lista_ventas_de_regiones[i]}")
            print(f"Porcentaje: {lista_porcentajes_de_regiones[i]}%")
            ventas_acumuladas += int(lista_ventas_de_regiones[i])
            regiones_acumuladas += 1

    print(f"\nVENTAS ACUMULADAS DE LA BUSQUEDA: {ventas_acumuladas}")
    print(f"CANTIDAD DE REGIONES DE LA BUSQUEDA: {regiones_acumuladas}")
    print(f"PROMEDIO DE VENTAS DE LA BUSQUEDA: {ventas_acumuladas / regiones_acumuladas}")

def mostrar_ventas_mayores_al_promedio(lista_ventas_de_regiones:list, lista_porcentajes_de_regiones:list, limite:int) -> None:
    """Muestra las ventas que coincidan con el dato ingresado."""
    porcentaje_acumulado = 0
    for i in range(len(lista_ventas_de_regiones)):
        if lista_ventas_de_regiones[i] > limite:
            print(f"\nREGIÓN N° {i + 1}")
            print(f"Ventas: {lista_ventas_de_regiones[i]}")
            print(f"Porcentaje: {lista_porcentajes_de_regiones[i]}%")
            porcentaje_acumulado += float(lista_porcentajes_de_regiones[i])

    print(f"\nPROMEDIO GENERAL DE TODAS LAS VENTAS: {calcular_total_de_lista(lista_ventas_de_regiones) / len(lista_ventas_de_regiones)}")
    print(f"PORCENTAJE ACUMULADO DE LA BUSQUEDA: {porcentaje_acumulado}")

def calcular_mayor_en_lista(lista:list) -> int:
    """Calcula cual es el numero mayor en una lista. Devuelve ese numero."""
    mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def mostrar_ventas_mas_grandes(lista_ventas_de_regiones:list, lista_porcentajes_de_regiones:list) -> None:
    """Muestra las ventas que coincidan con el dato ingresado."""
    mayor = calcular_mayor_en_lista(lista_ventas_de_regiones)
    for i in range(len(lista_ventas_de_regiones)):
        if lista_ventas_de_regiones[i] == mayor:
            print(f"\nREGIÓN N° {i + 1}")
            print(f"Ventas: {lista_ventas_de_regiones[i]}")
            print(f"Porcentaje: {lista_porcentajes_de_regiones[i]}%")

def ordenar_lista(lista:list) -> list:
    """Ordena una lista alfabeticamente."""
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                aux = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = aux
    return lista