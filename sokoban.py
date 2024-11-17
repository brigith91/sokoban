"""
Juego de Sokoban en consola
Este código permite al jugador mover un personaje dentro de un tablero para empujar cajas hacia sus posiciones de destino.
El jugador gana cuando todas las cajas están en los destinos.

Las funcionalidades del código incluyen:
1. Movimiento del jugador dentro del tablero.
2. Empujar cajas hacia los destinos.
3. Comprobación de si el jugador ha ganado.
4. Interacción con el tablero de manera visual a través de la consola.
"""

import os
import elemento
import movimiento as mv


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
"""
    Esta función limpia la pantalla en función del sistema operativo.
    usando el comando 'cls' y 'clear'.
"""

# 1 imprimir el tablero


def imprimir_tablero(tablero):
    """
    Imprime el tablero en la consola con numeración en las filas y columnas para facilitar la visualización.
    el tablero (list): Es una lista bidimensional que representa el estado del tablero de juego.
    """
    limpiar_pantalla()
    print('      ', end='')
    for i in range(len(tablero[0])):
        print(i + 1, end='   ')
    print()

    for i, fila in enumerate(tablero):
        print(f'{i + 1} - | ', end='')
        for columna in fila:
            print(f'{columna} | ', end='')
        print(f'- {i + 1}')

    print('      ', end='')
    for i in range(len(tablero[0])):
        print(i + 1, end='   ')
    print()

# 2 buscar la posición del jugador


def buscar_jugador(tablero):
    """
    Busca la posición del jugador en el tablero y retorna las coordenadas (fila, columna).
    tablero (list): Lista bidimensional que representa el estado del tablero de juego. 
    Retorna:
    tuple: Una tupla con las coordenadas (fila, columna) donde se encuentra el jugador.
    """
    for i, fila in enumerate(tablero):
        for j, columna in enumerate(fila):
            if columna == elemento.JUGADOR or columna == elemento.JUG_DEST:
                return i, j
    return -1, -1

def mover_jugador(tablero, direccion): 
    """
    Mueve al jugador en la dirección indicada y actualiza el tablero.
    Maneja correctamente los destinos y las cajas para evitar errores al pasar por un destino.
    
    tablero: lista bidimensional que representa el estado del tablero de juego.
    direccion (str): La dirección en la que el jugador se moverá (ARRIBA, ABAJO, IZQUIERDA, DERECHA).
    """
    # Posición actual del jugador
    fila, columna = buscar_jugador(tablero)
    fila_obj, columna_obj = fila, columna

    if direccion == mv.ARRIBA:
        fila_obj -= 1
    elif direccion == mv.ABAJO:
        fila_obj += 1
    elif direccion == mv.IZQUIERDA:
        columna_obj -= 1
    elif direccion == mv.DERECHA:
        columna_obj += 1
    else:
        print('Dirección no reconocida')
        return

    # Movimiento dentro del tablero
    if fila_obj < 0 or columna_obj < 0 or fila_obj >= len(tablero) or columna_obj >= len(tablero[0]):
        print('Movimiento no válido')
        return

    # Caso 1: objetivoun espacio vacío o un destino
    if tablero[fila_obj][columna_obj] in [elemento.ESP_VAC, elemento.DESTINO]:
        # Actualiza la posición actual del jugador
        tablero[fila][columna] = elemento.DESTINO if tablero[fila][columna] == elemento.JUG_DEST else elemento.ESP_VAC
        # Mueve al jugador
        tablero[fila_obj][columna_obj] = elemento.JUG_DEST if tablero[fila_obj][columna_obj] == elemento.DESTINO else elemento.JUGADOR

    # Caso 2: La celda objetivo es una caja o una caja en destino
    elif tablero[fila_obj][columna_obj] in [elemento.CAJA, elemento.CAJ_DEST]:
        # Verifica si la caja ya está en su destino
        if tablero[fila_obj][columna_obj] == elemento.CAJ_DEST:
            print("La caja ya está en un destino y no puede moverse.")
            return

        # Calcula la posición futura de la caja
        fila_caja_obj = fila_obj + (fila_obj - fila)
        columna_caja_obj = columna_obj + (columna_obj - columna)

        # Verifica si la celda futura de la caja está dentro de los límites y es válida
        if (0 <= fila_caja_obj < len(tablero) and 0 <= columna_caja_obj < len(tablero[0]) and
                tablero[fila_caja_obj][columna_caja_obj] in [elemento.ESP_VAC, elemento.DESTINO]):
            # Mueve la caja a su nueva posición
            tablero[fila_caja_obj][columna_caja_obj] = (
                elemento.CAJ_DEST if tablero[fila_caja_obj][columna_caja_obj] == elemento.DESTINO else elemento.CAJA
            )
            # Actualiza la posición actual de la caja
            tablero[fila_obj][columna_obj] = (
                elemento.DESTINO if tablero[fila_obj][columna_obj] == elemento.CAJ_DEST else elemento.ESP_VAC
            )
            # Mueve al jugador a la posición de la caja original
            tablero[fila][columna] = (
                elemento.DESTINO if tablero[fila][columna] == elemento.JUG_DEST else elemento.ESP_VAC
            )
            tablero[fila_obj][columna_obj] = elemento.JUG_DEST if tablero[fila_obj][columna_obj] == elemento.DESTINO else elemento.JUGADOR
        else:
            print('Movimiento no válido: la caja no puede moverse')

    # Caso 3: La celda objetivo no es válida (pared u otro elemento)
    else:
        print('Movimiento bloqueado: no se puede avanzar en esta dirección')

def mover_caja(tablero, fila_caja, columna_caja, direccion):
    """
    Mueve la caja en la dirección indicada por el movimiento del jugador y actualiza el tablero.
    tablero (list): Lista bidimensional que representa el estado del tablero de juego.
    fila_caja (int): Fila donde se encuentra la caja.
    columna_caja (int): Columna donde se encuentra la caja.
    direccion (str): Dirección en la que se mueve la caja ('ARRIBA', 'ABAJO', 'IZQUIERDA', 'DERECHA').
    """
    fila_caja_obj, columna_caja_obj = fila_caja, columna_caja

    if direccion == mv.ARRIBA:
        fila_caja_obj -= 1
    elif direccion == mv.ABAJO:
        fila_caja_obj += 1
    elif direccion == mv.IZQUIERDA:
        columna_caja_obj -= 1
    elif direccion == mv.DERECHA:
        columna_caja_obj += 1

    if fila_caja_obj < 0 or columna_caja_obj < 0 or fila_caja_obj >= len(tablero) or columna_caja_obj >= len(tablero[0]):
        print('Movimiento no válido')
        return

    if tablero[fila_caja_obj][columna_caja_obj] == elemento.ESP_VAC or tablero[fila_caja_obj][columna_caja_obj] == elemento.DESTINO:
        if tablero[fila_caja][columna_caja] == elemento.CAJ_DEST:
            tablero[fila_caja][columna_caja] = elemento.DESTINO
        else:
            tablero[fila_caja][columna_caja] = elemento.ESP_VAC
        tablero[fila_caja_obj][columna_caja_obj] = elemento.CAJA if tablero[
            fila_caja_obj][columna_caja_obj] == elemento.ESP_VAC else elemento.CAJ_DEST
        # Mueve al jugador a la posición de la caja empujada
        mover_jugador(tablero, direccion)


def leer_direccion():
    """
    Lee la dirección del movimiento que ingresa el jugador.
    Retorna:
    str: La dirección ingresada por el jugador ('W', 'A', 'S', 'D', 'X').
    """
    direccion = input(
        'Ingrese el movimiento (W:arriba /A:Abajo /S:Izquierda /D:Derecha) o X para salir : ').upper()
    if direccion in ['W', 'A', 'S', 'D', 'X']:
        return direccion
    else:
        return leer_direccion()


def win(tablero):
    """
    Compara si el jugador ha ganado verificando si todas las cajas están en los destinos.
    tablero (list): Lista bidimensional que representa el estado del tablero de juego.
    Retorna:
    bool: True si el jugador ha ganado, False en caso contrario.
    """
    # Recorre todo el tablero buscando cajas
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            if tablero[fila][columna] == elemento.CAJA:  # Si encuentra una caja
                # Verifica si la caja no está en un destino
                if tablero[fila][columna] != elemento.DESTINO:  # Compara si la caja no está en su destino
                    return False

    # Si todas las cajas están en los destinos
    return True


def juego():
    """
    Función principal del juego. Ejecuta el ciclo de juego, mostrando el tablero, permitiendo
    al jugador realizar movimientos y verificando si ha ganado.
    """
    
    tab = elemento.tablero
    imprimir_tablero(tab)
    direccion = leer_direccion()

    while direccion != mv.EXIT and not win(tab):
        mover_jugador(tab, direccion)
        imprimir_tablero(tab)
        direccion = leer_direccion()

    print('Ganaste')

def manual(idioma): 
    """
    Muestra el manual del juego en el idioma seleccionado.
    
    Args:
    idioma (str): El idioma en el que se debe mostrar el manual. 
    Puede ser 'es' para español o 'en' para inglés.
    
    El manual incluye una breve descripción del juego y la explicación de los elementos del tablero.
    Los elementos incluyen la pared, las cajas, los destinos, el jugador, los espacios vacíos, y los objetos en destino.
    """

    menu_manual = {
        'es' : {
            'desc': 'El juego consiste en recorrer todo el tablero ',
            elemento.PARED :    'Esta es la pared ',
            elemento.CAJA :     'Esta es la caja',
            elemento.DESTINO :  'Este es el destino',
            elemento.JUGADOR :  'Este es el jugador',
            elemento.ESP_VAC :  'Este es el espacio vacío',
            elemento.CAJ_DEST : 'Esta es la caja en destino',
            elemento.JUG_DEST : 'Este el jugador en destino',
        },

        'en' : {
            'desc':' You have to move around the full board',
            elemento.PARED :   'This is the wall',
            elemento.CAJA :    'This is the box',
            elemento.DESTINO : 'This is the destination',
            elemento.JUGADOR : 'This is the player',
            elemento.ESP_VAC : 'This is the empty space',
            elemento.CAJ_DEST :'This is the box at the destinationl',
            elemento.JUG_DEST :'This the player at the destination',
        },

    }

    for k in menu_manual[idioma]:
        if k != 'desc':
            print(f'\t{k} - {menu_manual[idioma][k]}')
        else:
            print(menu_manual[idioma])
    
    input()


def menu():
    """
    Muestra el menú principal y permite al jugador seleccionar una operación.El menú ofrece 3 opciones :
    
    El idioma del menú es seleccionado por el jugador al inicio y puede ser español ('es') o inglés ('en').
    Según la selección, las opciones y los mensajes se muestran en el idioma correspondiente.
    """
    mi_menu = {
        'es' : {
        '1' : 'Iniciar juego nuevo',
        '2' : 'Ver manual de juego',
        '3' : 'Salida'
        },
        'en' : {
        '1' : 'Start new game',
        '2' : 'Show manual',
        '3' : 'Exit'
        },
    }
    print('--------------------------------')
    lang = input('Indique el idioma (en/es): ').lower()

    if lang not in mi_menu:
        print('Idioma no válido. Por favor, ingrese "en" o "es".')
        menu()  # Si el idioma no es válido, vuelve a mostrar el menú
        return

    for k in mi_menu[lang]:
        print(f'{k}, {mi_menu[lang][k]} ')

    print('--------------------------------')
    if lang == 'es':
        opt = input('Ingrese la operación de preferencia: ').upper()
    else:
        opt = input('Enter your preferred operation: ').upper() 


    if opt == '1':
        juego()
    if opt == '2':
        manual(lang)
    elif opt == '3':
         print('Nos vemos la próxima.' if lang == 'es' else 'See you next time.')

menu()