import csv

with open("juegos.csv", "r", encoding="utf-8-sig") as archivo_juegos:
    traductor_juegos = csv.reader(archivo_juegos)
    lista_juegos = list(traductor_juegos)

lista_juego_filtrado = []
lista_precio_consolas = []
lista_juego_annio = []


while True:
    print('''
***MENU PRINCIPAL***
1) Filtro palabra
2) Promedio por consola
3) Cantidad de juegos por año
4) Salir
''')
    opcion_menu_elegida = input("Ingrese una opcion: ")
    #Salir del sistema
    if opcion_menu_elegida == "4":
        print("Saliendo del sistema...")
        break
    #Filtrar palabra
    elif opcion_menu_elegida == "1":
        buscar_nombre = input("Ingrese palabra a buscar: ")
        for i in lista_juegos:
            juego, cantidad_jugadores, precio, consola, annio = i
            if buscar_nombre.lower() in juego.lower():
                lista_juego_filtrado.append(juego+"\n")
                print(lista_juego_filtrado[0:5])
                with open("filtro_por_nombre.txt", "w", encoding="utf-8-sig") as archivo_juegos_buscados:
                    archivo_juegos_buscados.writelines(lista_juego_filtrado)
        else:
            print("No hay títulos con esa palabra")
    #Promedio por consola
    elif opcion_menu_elegida == "2":
        buscar_precio = input("Ingrese el nombre de la consola: ")
        for i in lista_juegos:
            juego, cantidad_jugadores, precio, consola, annio = i
            if buscar_precio.lower() == consola.lower():
                lista_precio_consolas.append(float(precio))
        print(f"El precio de la consola {buscar_precio} es {sum(lista_precio_consolas)}")
    #Cantidad de juegos por año
    elif opcion_menu_elegida == "3":
        ingresar_annio = input("Ingrese año a consultar: ")
        for i in lista_juegos:
            juego, cantidad_jugadores, precio, consola, annio = i
            if ingresar_annio == annio:
                lista_juego_annio.append(annio)
                cantidad_juegos = lista_juego_annio.count(ingresar_annio)
            with open("juegos_AÑO.txt", "w", encoding="utf-8-sig") as archivo_datos_consolas:
                archivo_datos_consolas.writelines(f"La consola {consola} tuvo {cantidad_juegos} juegos")
        print(cantidad_juegos)
        print(f"La consola {consola} tuvo {cantidad_juegos} juegos")


