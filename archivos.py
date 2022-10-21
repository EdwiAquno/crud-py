def leer_archivos(file_name):
    print(f'intentas abrir este rchivo {file_name}')
    # Abrir open()
    #prosesar red/write
    #cerrar close()
    #with nos permite agrupar el trabajo con archivos
    with open(file_name, 'r') as file:
        lineas = file.readlines()
        for linea in lineas :
           print(linea, end='')
        #while(linea):
        #    print(linea)
         #   linea = file.readline()
    #print('archivo leido y serrado')        

def agregar_equipo(file_name, equipo):
    with open(file_name, 'a') as file:
        file.write(f"\n{equipo}")
        print('equipo guardado ')

def eliminar_equipo(file_name, equipo):
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()
    try:
        lista_equipos.remove(equipo)
        print("equipo eliminado")
        with open(file_name, 'w') as file:
            file.writelines(lista_equipos)
    except ValueError:
        print("el equipo no existe")        