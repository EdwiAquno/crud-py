'''lista_elements = [
    {
        "id": 1,
        "name": "Francisco",
        "last_name": "Lopez"
    },
    {
        "id": 2,
        "name": "Pedro",
        "last_name": "Perez"
    }
]'''

import json
from xml.dom.minidom import Identified
with open('elemento.json', 'r') as file:
    lista_elements =json.load(file)

def add_element():
    id = int(input('Ingresa el ID de la persona: '))
    name = input("Ingresa el nombre de la persona: ")
    last_name = input('Ingresa el apellido de la persona: ')
    person = {
        "id": id,
        "name": name,
        "last_name": last_name
    }
    lista_elements.append(person)
    guardar_lista()

def remove_element():
    id = int(input('Ingresa el ID del elemento a Eliminar: '))
    found = find_element(id)
    if found:
        print(found)
        aceptar = input("Estás seguro? (S/N)")
        if aceptar == "S":
            lista_elements.remove(found)
            print("Elemento Eliminado")
            guardar_lista()
    else:
        print(f"El elemento  no existe{id} no existe")

def find_element(id):
   
    for element in lista_elements:
        if element['id'] == id:
        
           return element

def show_elements():
    # for para iterar y mostrar
    for element in lista_elements:
        print(f"Alumno: {element['name']} {element['last_name']}")
        '''for key, value in element.items():
            print(f"{key} -> {value}")'''

def edit_element():
    id = int(input('Ingresa el ID del elemento a editar: '))
    found = find_element(id)
    if found:
        print(found)
        index =lista_elements.index(found)
        name =input("ingresa el nombre, deja en blanco para conservar: /n")
        last_name = input("ingresa el nuevo apellido, deja en blanco para conservar: /n")
        if name != '':
            lista_elements[index]['name'] = name
        if last_name != '':
            lista_elements[index]['last_name'] = last_name
            guardar_lista()
    else:
        print(f"El elemento  no existe{id} no existe")        

    '''name = input("Ingresa el nuevo nombre de la persona: ")
    last_name = input('Ingresa el nuevo apellido de la persona: ')
    person = {
        "id": id,
        "name": name,
        "last_name": last_name
    }
    lista_elements.remove(found)
    lista_elements.append(person)'''

def guardar_lista():
    with open('elemto.json', 'w') as file:
        json.dump(lista_elements, file, Indent=4)

if __name__ == '__main__':
    menu = '''
    Implementación de CRUD de Elementos:
    Elige una Opción
    1 - Insertar
    2 - Mostrar todos
    3 - Buscar por ID
    4 - Editar
    5 - Eliminar
    6 - Salir
    '''
    while True:
        opcion = input(menu)
        if opcion == '1':
            print("Insertar Elemento")
            add_element()
        elif opcion == '2':
            print("Mostrar todos los elementos")
            show_elements()
        elif opcion == '3':
            print("Busca por ID")
            id = int(input("Ingresa el ID a buscar: "))
            found = find_element(id)
            if found:
                print(found)
        elif opcion == '4':
            print("Editar Elemento")
            edit_element()
        elif opcion == '5':
            print("Eliminar Elemento")
            remove_element()
        elif opcion == '6':
            print('Bye!')
            break
        else:
            print("Opción Incorrecta!")
