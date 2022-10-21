
lista_elements= [ {
         "nombre": "",
         "tamaño": ""
         },
         {
        "nombre": "",
         "tamaño": ""
         }
         ]

def add_element():
    
    lista_elements.append(lista_elements= [ {
         "nombre": "",
         "tamaño": ""
         },
         {
        "nombre": "",
         "tamaño": ""
         }
         ]
        
    )
    pass
def remove_element():
    #for para buscar 
    lista_elements.remove({
        "nombre": ""
    })
    pass
def show_element():
    #for para buscar
    pass
def show_elements():
    for element in lista_elements:
        if element ['nombre'] == entrada:
            element_buscado = element_buscado
        return element_buscado
    #for para iterarar y mostrar
    pass
def edit_element():
    #ror para buscar 
    #editar
    pass

if __name__ =='__main__':
    print("muestra menu")
    message = message = f"Crud: \n Elige una opcion\n 1 - agragar\n 2 - remover\n 3 - buscar\n 4 - editar\n5 - salir\n"
    

    while True:
        opcion = int(input(message))
        if  opcion == 1:
          add_element()
          for element in lista_elements:
            element ['nombre'] = input("agrega un nombre: ")
            element ['tamaño'] = input("agrega un tamaño: ")
   
            
            
            print("agregado")
        elif  opcion == 2:
             print("hola")
          
        elif  opcion == 3:
            entrada = input("nombre del elemento : ")
            show_elements()
            
        elif  opcion == 4:
            entrada = input("nombre del elemento : ")
            opjeto =show_elements()
            
        elif  opcion == 5:
            print('bye')
            break

