PARED = '🧱'  # símbolo de pared lleno
CAJA = '📦'   # símbolo de caja
DESTINO = '⭕'  # símbolo de destino, como una bandera
JUGADOR = '🙂'  # símbolo de jugador, como una cara
ESP_VAC = ' 🕸'  # espacio vacío sin punto
CAJ_DEST = '🎲'  # caja en destino (puedes combinarlos si quieres)
JUG_DEST = '👩‍💼'  # jugador en destino

tablero = (
    [PARED, PARED, PARED, PARED, PARED, PARED, PARED],
    [PARED, ESP_VAC, ESP_VAC, DESTINO, ESP_VAC, ESP_VAC, PARED],
    [PARED, ESP_VAC, CAJA, CAJA, DESTINO, ESP_VAC, PARED],
    [PARED, ESP_VAC, ESP_VAC, JUGADOR, ESP_VAC, ESP_VAC, PARED],
    [PARED, PARED, PARED, ESP_VAC, PARED, PARED, PARED],
    [PARED, ESP_VAC, ESP_VAC, ESP_VAC, ESP_VAC, ESP_VAC, PARED],
    [PARED, PARED, PARED, PARED, PARED, PARED, PARED],
)
