""" CLASE Mapa:
    ATRIBUTOS:
        - filas: entero
        - columnas: entero
        - matriz: arreglo 2D
        - inicio: tupla (fila, columna)
        - fin: tupla (fila, columna)
    
    MÉTODO __init__(filas, columnas, inicio, fin):
        1. Asignar filas y columnas
        2. Validar que inicio y fin estén dentro de los límites
        3. Crear matriz vacía de tamaño filas x columnas
        4. Inicializar todas las celdas con '.'
        5. Marcar posición inicio con 'I'
        6. Marcar posición fin con 'F'
    
    MÉTODO mostrar_mapa():
        1. PARA cada fila EN matriz:
            2. Imprimir fila completa
    
    MÉTODO validar_coordenadas(fila, columna):
        1. SI fila >= 0 Y fila < filas Y columna >= 0 Y columna < columnas:
            2. RETORNAR Verdadero
        3. SINO:
            4. RETORNAR Falso

PROGRAMA PRINCIPAL:
    1. Solicitar al usuario número de filas
    2. Solicitar al usuario número de columnas
    3. Solicitar coordenadas de inicio (fila, columna)
    4. Solicitar coordenadas de fin (fila, columna)
    5. Crear objeto Mapa con los datos ingresados
    6. Mostrar el mapa en pantalla """
""" CLASE Mapa:
    # ... atributos y métodos anteriores ...
    
    
    MÉTODO AgregarObstaculos():
        '''
        Método principal que solicita datos y agrega obstáculos
        '''
        1. SI inicio o fin NO están definidos:
            2. IMPRIMIR "Error: Define inicio y fin primero"
            3. RETORNAR False
        
        4. Solicitar cantidad_agua al usuario
        5. Solicitar cantidad_edificios al usuario
        
        6. total_obstaculos = cantidad_agua + cantidad_edificios
        7. celdas_disponibles = (filas × columnas) - 2
        
        8. SI total_obstaculos >= celdas_disponibles:
            9. IMPRIMIR "Demasiados obstáculos para el tamaño del mapa"
            10. RETORNAR False
        
        11. IMPRIMIR "Colocando obstáculos..."
        
        # Colocar obstáculos de agua
        12. PARA i desde 0 hasta cantidad_agua - 1:
            13. SI NO ColocarObstaculoSeguro("~"):
                14. IMPRIMIR "No se pudo colocar obstáculo de agua"
                15. ROMPER bucle
        
        # Colocar obstáculos de edificios
        16. PARA i desde 0 hasta cantidad_edificios - 1:
            17. SI NO ColocarObstaculoSeguro("X"):
                18. IMPRIMIR "No se pudo colocar obstáculo de edificio"
                19. ROMPER bucle
        
        20. RETORNAR True
    
    
    MÉTODO ColocarObstaculoSeguro(simbolo):
        '''
        Intenta colocar un obstáculo manteniendo camino válido
        '''
        1. intentos = 0
        2. max_intentos = filas × columnas × 2
        
        3. MIENTRAS intentos < max_intentos:
            4. fila = número aleatorio entre 0 y filas - 1
            5. columna = número aleatorio entre 0 y columnas - 1
            
            6. SI CeldaEsValida(fila, columna):
                # Guardar estado actual
                7. valor_anterior = mapa[fila][columna]
                
                # Colocar obstáculo temporalmente
                8. mapa[fila][columna] = simbolo
                
                # Verificar si aún hay camino
                9. SI ExisteCamino():
                    10. RETORNAR True  # Obstáculo colocado exitosamente
                SINO:
                    # Restaurar estado anterior
                    11. mapa[fila][columna] = valor_anterior
            
            12. intentos = intentos + 1
        
        13. RETORNAR False  # No se pudo colocar
    
    
    MÉTODO CeldaEsValida(fila, columna):
        '''
        Verifica si una celda puede tener un obstáculo
        '''
        1. SI NOT ValidarCoord(fila, columna):
            2. RETORNAR False
        
        3. SI (fila, columna) == inicio:
            4. RETORNAR False
        
        5. SI (fila, columna) == fin:
            6. RETORNAR False
        
        7. SI mapa[fila][columna] != ".":
            8. RETORNAR False
        
        9. RETORNAR True
    
    
    MÉTODO ExisteCamino():
        '''
        Verifica si existe un camino de inicio a fin usando BFS
        (Búsqueda en Anchura)
        '''
        1. SI inicio es None O fin es None:
            2. RETORNAR False
        
        3. fila_inicio, col_inicio = inicio
        4. fila_fin, col_fin = fin
        
        # Inicializar BFS
        5. cola = nueva Cola()
        6. cola.agregar(inicio)
        
        7. visitados = conjunto vacío
        8. visitados.agregar(inicio)
        
        # BFS
        9. MIENTRAS cola NO está vacía:
            10. fila_actual, col_actual = cola.extraer()
            
            # Si llegamos al fin
            11. SI (fila_actual, col_actual) == fin:
                12. RETORNAR True
            
            # Explorar vecinos (arriba, abajo, izquierda, derecha)
            13. direcciones = [(-1,0), (1,0), (0,-1), (0,1)]
            
            14. PARA cada (df, dc) EN direcciones:
                15. nueva_fila = fila_actual + df
                16. nueva_col = col_actual + dc
                
                17. SI ValidarCoord(nueva_fila, nueva_col):
                    18. SI (nueva_fila, nueva_col) NO está en visitados:
                        19. celda = mapa[nueva_fila][nueva_col]
                        
                        # Solo celdas transitables
                        20. SI celda == "." O celda == "S" O celda == "I":
                            21. visitados.agregar((nueva_fila, nueva_col))
                            22. cola.agregar((nueva_fila, nueva_col))
        
        23. RETORNAR False  # No hay camino
    
    
    MÉTODO ObtenerVecinos(fila, columna):
        '''
        Retorna lista de coordenadas vecinas válidas
        (Método auxiliar útil)
        '''
        1. vecinos = lista vacía
        2. direcciones = [(-1,0), (1,0), (0,-1), (0,1)]
        
        3. PARA cada (df, dc) EN direcciones:
            4. nueva_fila = fila + df
            5. nueva_col = columna + dc
            
            6. SI ValidarCoord(nueva_fila, nueva_col):
                7. vecinos.agregar((nueva_fila, nueva_col))
        
        8. RETORNAR vecinos """