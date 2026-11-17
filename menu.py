from funciones import *
def prender_menu():
    condicion_de_continuidad_menu = True
    existencia_de_lista = False
    while condicion_de_continuidad_menu:
        limpiar_terminal()
        mostrar_titulo("SISTEMA DE GESTIÓN DE VENTAS")
        mostrar_opciones()
        opcion = input("\nIngrese una opción: ")
        match opcion:
            case "1":
                lista_nombres_de_regiones = []
                lista_ventas_de_regiones = []
                lista_porcentajes_de_regiones = []
                vueltas = 0
                while vueltas < 6:
                    limpiar_terminal()
                    mostrar_titulo("CARGAR VENTAS")
                    vueltas += 1
                    ventas_de_region = input(f"\nIngrese la cantidad de ventas de la region N° {vueltas}: ")
                    while not validar_numero_entero_positivo(ventas_de_region) or ventas_de_region == "0" or ventas_de_region == "":
                        print("\nEntrada invalida.")
                        ventas_de_region = input(f"\nIngrese la cantidad de ventas del region N° {vueltas}: ")
                    lista_ventas_de_regiones.append(ventas_de_region)
                lista_porcentajes_de_regiones = calcular_porcentajes_de_lista(lista_ventas_de_regiones)
                existencia_de_lista = True

            case "2":
                limpiar_terminal()
                mostrar_titulo("MOSTRAR VENTAS")
                if existencia_de_lista:
                    mostrar_ventas(lista_ventas_de_regiones, lista_porcentajes_de_regiones)
                    input("\nOprima cualquier tecla para continuar..")
                else:
                    print("\nNo se cargaron ventas.")
                    input("Oprima cualquier tecla para continuar..")

            case "3":
                limpiar_terminal()
                mostrar_titulo("REGIONES CON MENOS DEL 5% DE VENTAS")
                if existencia_de_lista:
                    if validar_existencia_de_elemento_menor_en_lista(lista_porcentajes_de_regiones, 5):
                        mostrar_ventas_menores_a_numero(lista_ventas_de_regiones, lista_porcentajes_de_regiones, 5)
                        
                    else:
                        print("\nNo se encontraron datos que coincidan con la busqueda")
                    input("\nOprima cualquier tecla para continuar..")
                else:
                    print("\nNo se cargaron ventas.")
                    input("\nOprima cualquier tecla para continuar..")            
            case "4":
                limpiar_terminal()
                mostrar_titulo("REGIONES CON MENOS DEL 25% DE VENTAS")
                if existencia_de_lista:
                    if validar_existencia_de_elemento_menor_en_lista(lista_porcentajes_de_regiones, 25):
                        mostrar_ventas_menores_a_numero(lista_ventas_de_regiones, lista_porcentajes_de_regiones, 25)
                    else:
                        print("\nNo se encontraron datos que coincidan con la busqueda")
                    input("\nOprima cualquier tecla para continuar..")
                else:
                    print("\nNo se cargaron ventas.")
                    input("\nOprima cualquier tecla para continuar..")
            case "5":
                limpiar_terminal()
                mostrar_titulo("REGIONES CON MAS DE 500 VENTAS")
                if existencia_de_lista:
                    if validar_existencia_de_elemento_mayor_en_lista(lista_ventas_de_regiones, 500):
                        mostrar_ventas_mayores_a_numero(lista_ventas_de_regiones, lista_porcentajes_de_regiones, 500)
                    else:
                        print("\nNo se encontraron datos que coincidan con la busqueda")
                    input("\nOprima cualquier tecla para continuar..")
                else:
                    print("\nNo se cargaron ventas.")
                    input("\nOprima cualquier tecla para continuar..")     
            case "6":
                limpiar_terminal()
                mostrar_titulo("REGIONES CON MAS DE 3000 VENTAS")
                if existencia_de_lista:
                    if validar_existencia_de_elemento_mayor_en_lista(lista_ventas_de_regiones, 3000):
                        mostrar_ventas_mayores_a_numero(lista_ventas_de_regiones, lista_porcentajes_de_regiones, 3000)
                    else:
                        print("\nNo se encontraron datos que coincidan con la busqueda")
                    input("\nOprima cualquier tecla para continuar..")
                else:
                    print("\nNo se cargaron ventas.")
                    input("\nOprima cualquier tecla para continuar..")   
            case "7":
                limpiar_terminal()
                mostrar_titulo("REGIONES POR ARRIBA DEL PROMEDIO DE VENTAS")
                if existencia_de_lista:
                    promedio = calcular_total_de_lista(lista_ventas_de_regiones) / len(lista_ventas_de_regiones)
                    if validar_existencia_de_elemento_mayor_en_lista(lista_ventas_de_regiones, promedio):
                        mostrar_ventas_mayores_al_promedio(lista_ventas_de_regiones, lista_porcentajes_de_regiones, promedio)
                    else:
                        print("\nNo se encontraron datos que coincidan con la busqueda")
                    input("\nOprima cualquier tecla para continuar..")
                else:
                    print("\nNo se cargaron ventas.")
                    input("\nOprima cualquier tecla para continuar..")
            case "8":
                limpiar_terminal()
                mostrar_titulo("REGION/ES MÁS COMPRADORA/S")
                if existencia_de_lista:
                    mostrar_ventas_mas_grandes(lista_ventas_de_regiones, lista_porcentajes_de_regiones)
                    input("\nOprima cualquier tecla para continuar..")
                else:
                    print("\nNo se cargaron ventas.")
                    input("\nOprima cualquier tecla para continuar..")
            case "9":
                limpiar_terminal()
                mostrar_titulo("HARDCODEAR VECTOR")
                lista_ventas_de_regiones = [1800, 555, 2333, 1850, 3999, 777, 1410, 7180, 2500, 60]
                lista_nombres_de_regiones = ["PBA", "CABA", "La Pampa", "Tucuman", "Mendoza", "Chubut", "Corrientes", "Neuquén", "La Rioja", "Jujuy"]
                lista_porcentajes_de_regiones = calcular_porcentajes_de_lista(lista_ventas_de_regiones)
                existencia_de_lista = True
                print("\nVector hardcodeado.")
                input("\nOprima cualquier tecla para continuar..")
            case "10":
                limpiar_terminal()
                mostrar_titulo("ORDENAR REGIONES")
                if len(lista_nombres_de_regiones) == 0:
                    print("\nNo se cargaron nombres.")
                    input("\nOprima cualquier tecla para continuar..")
                else:
                    print("\nRegiones sin ordenar")
                    print(f"\n{lista_nombres_de_regiones}")
                    print("\nRegiones ordenadas")
                    print(f"\n{ordenar_lista(lista_nombres_de_regiones)}")
                    input("\nOprima cualquier tecla para continuar..")

            case "11":
                print("\nSaliendo.")
                input("\nOprima cualquier tecla para continuar..")
                condicion_de_continuidad_menu = False
            case _:
                print("\nEntrada invalida.")
                input("\nOprima cualquier tecla para continuar..")