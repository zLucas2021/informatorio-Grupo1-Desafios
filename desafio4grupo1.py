#Creacion de Constante de los estados de los inmuebles
ESTADOS=['Disponible','Reservado','Vendido']
"""
    Parametros:
        lista: list
        inmueble: dict
    Funcion:
        añadir al inmueble a la lista si el mismo cuenta con las propiedades exactas
"""
def agregar(lista,inmueble):
    if controlar(inmueble) :
        lista.append(inmueble)
    else:
        print('Valores no validos en el inmueble')

"""
    Parametros:
        lista: list
        inmueble: dict
    Funcion:
        borrar al inmueble de la lista si el mismo se encuentra
"""
def remover(lista,inmueble):    
    if inmueble in lista:
        lista.remove(inmueble)
    else:
        print('No existe ese inmueble')

"""
    Parametros:
        lista: list
        inmueble: dict
        nuevoinmueble: dict
    Funcion:
        recorrer la lista , si se encuentra el inmueble anterior, lo modifica con el nuevo inmueble
"""
def modificar(lista,inmueble,nuevoinmueble):
    for i in range(len(lista)):
        if lista[i] == inmueble:
            if controlar(nuevoinmueble):
                lista[i] = nuevoinmueble
                return
            else:
                print('Valores no validos en el inmueble')

"""
    Parametros:
    inmueble: dict
    Funcion:
        Validar todas las condiciones del innmueble
"""
def controlar(inmueble):
    return inmueble.get('zona') in 'ABC' and inmueble.get('estado') in ESTADOS and inmueble.get('año') >=2000 and  inmueble.get('metros') >= 60 and inmueble.get('habitaciones') >=2
"""
    Parametros:
    lista:list
    inmueble: dict
    estado:str
    Funcion:
        Recorrer la lista y si encuentra el inmuble y a su ves el estado es correcto lo cambia
"""
def cambiarEstado(lista,inmueble,estado):
    for i in range(len(lista)) :
        if lista[i] == inmueble and estado in ESTADOS:
            lista[i]['estado'] = estado
            print('Cambio Realizado con exito')
            return
"""
    Parametros:
    lista:list
    precio:enum
    Funcion:
        Buscar en la lista un inmueble con un presupuesto menor o igual al pasado
        llamando a la funcion calcular precio
        """
def buscar(lista,precio):
    listInmueble = []
    for i in range(len(lista)):
        presupuesto = calcularprecio(lista[i])
        if presupuesto <= precio:
            inmueble = lista[i]
            inmueble.update({'precio':presupuesto})
            listInmueble.append(inmueble)
    return listInmueble
"""
    Parametros:
    inmueble:dict
    Funcion:
        Calcula el presupuesto d eun inmueble dado inmueble
        """
def calcularprecio(inmueble):
    if inmueble.get('zona') == 'A':
        precio = (inmueble.get('metros')*100 + inmueble.get('habitaciones')*500 + inmueble.get('garaje')*1500 ) * (1 - (2023-inmueble.get('año')) /100 )
    elif inmueble.get('zona') == 'B':
        precio = (inmueble.get('metros')*100 + inmueble.get('habitaciones')*500 + inmueble.get('garaje')*1500 ) * (1 - (2023-inmueble.get('año')) /100 ) * 1.5
    elif inmueble.get('zona') == 'C':
        precio = (inmueble.get('metros')*100 + inmueble.get('habitaciones')*500 + inmueble.get('garaje')*1500 ) * (1 - (2023-inmueble.get('año')) /100 ) * 2
    return precio

lista = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]


"""listaNueva = buscar(lista,20000)
print(f'Lista que se adecuan con el presupuesto: \n{listaNueva}')"""

"""cambiarEstado(lista,{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},'Reservado')
print(lista)"""

"""remover(lista,{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'})
print(lista)
agregar(lista,{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'})
print(lista)"""

"""modificar(lista , {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},{'año': 2020, 'metros': 200, 'habitaciones': 3, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'})
print(lista)"""
