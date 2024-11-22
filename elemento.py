PARED = '🧱'  # símbolo de pared 
CAJA = '📦'   # símbolo de caja
DESTINO = '⭕'  # símbolo de destino
JUGADOR = '🙂'  # símbolo de jugador
ESP_VAC = ' 🕸'  # espacio vacío 
CAJ_DEST = '🎲'  # caja en destino
JUG_DEST = '👩'  # jugador en destino


# Definición de símbolos
PARED = '🧱'  # símbolo de pared lleno
CAJA = '📦'   # símbolo de caja
DESTINO = '⭕'  # símbolo de destino, como una bandera
JUGADOR = '🙂'  # símbolo de jugador, como una cara
ESP_VAC = '🕸'  # espacio vacío sin punto
CAJ_DEST = '🎲'  # caja en destino
JUG_DEST = '👩'  # jugador en destino

def leer_tablero(nivel):
    tablero = []
    seccion = ''
    variables = {}

    # Abrir el archivo del nivel
    with open(f'{nivel}.elemento', 'r') as f:
        lineas = f.readlines()

        for linea in lineas:
            # Quitar el último carácter y espacios 
            linea = linea[:-1].strip()

            if linea in ('', '\n'):
                continue  # Ignorar líneas vacías
            if linea in ('# VARIABLES', '# TABLERO'):
                seccion = linea
                continue

            if seccion == '# VARIABLES':
                # Leer variables
                linea = linea.split('=')
                var = linea[0].strip()
                tipo = linea[1].strip()
                
                # variables al símbolo 
                if tipo == 'ESPACIO':
                    tipo = ESP_VAC
                elif tipo == 'JUGADOR':
                    tipo = JUGADOR
                elif tipo == 'MURO':
                    tipo = PARED
                elif tipo == 'CAJA':
                    tipo = CAJA
                elif tipo == 'DESTINO':
                    tipo = DESTINO
                elif tipo == 'CAJ_DEST':
                    tipo = CAJ_DEST
                elif tipo == 'JUG_DEST':
                    tipo = JUG_DEST

                variables[var] = tipo

            elif seccion == '# TABLERO':
                # Reemplaza las variables con sus símbolos en el tablero
                for var, tipo in variables.items():
                    linea = linea.replace(var, tipo)

                # Convierte la línea en una lista de caracteres y la agrega al tablero
                linea = list(linea)
                tablero.append(list(linea))

    return tablero

if __name__ == '__main__':
    tablero = leer_tablero('nivel_1')
