



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
    

CLASE PathFinder:
    '''
    Clase separada para algoritmos de búsqueda de caminos
    '''
    
    ATRIBUTOS:
        - mapa: referencia al objeto Mapa
        - filas: número de filas
        - columnas: número de columnas
    
    
    MÉTODO __init__(mapa):
        '''
        Constructor que recibe el objeto Mapa
        '''
        1. self.mapa = mapa
        2. self.filas = mapa.filas
        3. self.columnas = mapa.columnas
    
    
    MÉTODO ExisteCamino(inicio, fin):

CLASE PathFinder:
    '''
    Clase separada para algoritmos de búsqueda de caminos
    '''
    
    ATRIBUTOS:
        - mapa: referencia al objeto Mapa
        - filas: número de filas
        - columnas: número de columnas
    
    
    MÉTODO __init__(mapa):
        '''
        Constructor que recibe el objeto Mapa
        '''
        1. self.mapa = mapa
        2. self.filas = mapa.filas
        3. self.columnas = mapa.columnas
    
    
    MÉTODO ExisteCamino(inicio, fin):
        '''
        Verifica si existe un camino de inicio a fin usando Dijkstra
        '''
        1. camino = self.EncontrarCamino(inicio, fin)
        2. SI camino es None:
            3. RETORNAR False
        4. SINO:
            5. RETORNAR True
    
    
    MÉTODO EncontrarCamino(inicio, fin):
        '''
        Encuentra el camino más corto usando el algoritmo de Dijkstra
        Retorna: lista de coordenadas del camino, o None si no existe
        '''
        
        # Validar entrada
        Verifica si existe un camino de inicio a fin usando Dijkstra
        '''
        1. camino = self.EncontrarCamino(inicio, fin)
        2. SI camino es None:
            3. RETORNAR False
        4. SINO:
            5. RETORNAR True
    
    
    MÉTODO EncontrarCamino(inicio, fin):
        '''
        Encuentra el camino más corto usando el algoritmo de Dijkstra
        Retorna: lista de coordenadas del camino, o None si no existe
        '''
        
        # Validar entrada
        1. SI inicio es None O fin es None:
            2. RETORNAR None
            2. RETORNAR None
        
        3. fila_inicio, col_inicio = inicio
        4. fila_fin, col_fin = fin
        
        # Inicializar estructuras de Dijkstra
        5. distancias = diccionario con todas las celdas → infinito
        6. distancias[inicio] = 0
        # Inicializar estructuras de Dijkstra
        5. distancias = diccionario con todas las celdas → infinito
        6. distancias[inicio] = 0
        
        7. padres = diccionario vacío  # Para reconstruir el camino
        8. visitados = conjunto vacío
        
        9. cola_prioridad = nueva ColaPrioridad()
        10. cola_prioridad.agregar((0, inicio))  # (distancia, coordenada)
        7. padres = diccionario vacío  # Para reconstruir el camino
        8. visitados = conjunto vacío
        
        9. cola_prioridad = nueva ColaPrioridad()
        10. cola_prioridad.agregar((0, inicio))  # (distancia, coordenada)
        
        # Algoritmo de Dijkstra
        11. MIENTRAS cola_prioridad NO está vacía:
            12. distancia_actual, posicion_actual = cola_prioridad.extraer_minimo()
        # Algoritmo de Dijkstra
        11. MIENTRAS cola_prioridad NO está vacía:
            12. distancia_actual, posicion_actual = cola_prioridad.extraer_minimo()
            
            # Si ya visitamos esta celda, saltar
            13. SI posicion_actual EN visitados:
                14. CONTINUAR
            
            # Marcar como visitado
            15. visitados.agregar(posicion_actual)
            
            # Si llegamos al destino, reconstruir camino
            16. SI posicion_actual == fin:
                17. RETORNAR self.ReconstruirCamino(padres, inicio, fin)
            
            # Explorar vecinos
            18. vecinos = self.ObtenerVecinosTransitables(posicion_actual)
            
            19. PARA cada vecino EN vecinos:
                20. SI vecino NO está EN visitados:
                    # Calcular costo de llegar al vecino
                    21. costo_movimiento = self.ObtenerCosto(vecino)
                    22. nueva_distancia = distancia_actual + costo_movimiento
                    
                    # Si encontramos un camino mejor
                    23. SI nueva_distancia < distancias[vecino]:
                        24. distancias[vecino] = nueva_distancia
                        25. padres[vecino] = posicion_actual
                        26. cola_prioridad.agregar((nueva_distancia, vecino))
        
        # No se encontró camino
        27. RETORNAR None
    
    
    MÉTODO ObtenerVecinosTransitables(posicion):
        '''
        Retorna lista de vecinos transitables
        (no son obstáculos)
        '''
        1. fila, columna = posicion
        2. vecinos = lista vacía
        3. direcciones = [(-1,0), (1,0), (0,-1), (0,1)]  # arriba, abajo, izq, der
        
        4. PARA cada (df, dc) EN direcciones:
            5. nueva_fila = fila + df
            6. nueva_col = columna + dc
            
            7. SI self.ValidarCoordenada(nueva_fila, nueva_col):
                8. celda = self.mapa.mapa[nueva_fila][nueva_col]
                
                9. SI celda ES transitable (".", "I", "S"):
                    10. vecinos.agregar((nueva_fila, nueva_col))
        
        11. RETORNAR vecinos
    
    
    MÉTODO ValidarCoordenada(fila, columna):
        '''
        Verifica si la coordenada está dentro del mapa
        '''
        1. RETORNAR (0 <= fila < self.filas) Y (0 <= columna < self.columnas)
    
    
    MÉTODO ObtenerCosto(posicion):
        '''
        Retorna el costo de moverse a una celda
        Por defecto: 1 para todas las celdas
        Puede extenderse para diferentes costos
        '''
        1. RETORNAR 1
        
        # EXTENSIÓN FUTURA: diferentes costos
        # fila, columna = posicion
        # celda = self.mapa.mapa[fila][columna]
        # SI celda == "terreno difícil":
        #     RETORNAR 2
        # SI celda == "camino rápido":
        #     RETORNAR 0.5
        # SINO:
        #     RETORNAR 1
    
    
    MÉTODO ReconstruirCamino(padres, inicio, fin):
        '''
        Reconstruye el camino desde inicio hasta fin
        usando el diccionario de padres
        '''
        1. camino = lista vacía
        2. actual = fin
        
        3. MIENTRAS actual != inicio:
            4. camino.agregar(actual)
            
            5. SI actual NO está EN padres:
                6. RETORNAR None  # Error: camino incompleto
            
            7. actual = padres[actual]
        
        8. camino.agregar(inicio)
        9. camino.invertir()  # Para que vaya de inicio a fin
        
        10. RETORNAR camino
    
    
    MÉTODO VisualizarCamino(camino):
        '''
        Muestra el mapa con el camino marcado
        (útil para debugging)
        '''
        1. SI camino es None:
            2. IMPRIMIR "No hay camino"
            3. RETORNAR
        
        4. CREAR copia del mapa
        
        5. PARA cada (fila, columna) EN camino:
            6. SI NO es inicio ni fin:
                7. mapa_copia[fila][columna] = "*"
        
        8. MOSTRAR mapa_copia
        
CLASE Mapa:
    # ... atributos existentes ...
    
    MÉTODO __init__(filas, columnas):
        # ... código existente ...
        
        # Agregar instancia de PathFinder
        self.pathfinder = PathFinder(self)  # ← NUEVO
    
    
    MÉTODO ColocarObstaculoSeguro(simbolo):
        1. intentos = 0
        2. max_intentos = filas × columnas × 3
        
        3. MIENTRAS intentos < max_intentos:
            4. fila = aleatorio(0, filas-1)
            5. columna = aleatorio(0, columnas-1)
            
            6. SI CeldaEsValida(fila, columna):
                7. valor_anterior = mapa[fila][columna]
                8. mapa[fila][columna] = simbolo
                
                # Usar PathFinder para verificar
                9. SI self.pathfinder.ExisteCamino(self.inicio, self.fin):
                    10. RETORNAR True
                SINO:
                    11. mapa[fila][columna] = valor_anterior
            
            12. intentos += 1
        
        13. RETORNAR False
    
    
    MÉTODO MostrarCaminoOptimo():
        '''
        NUEVO: Muestra el camino más corto encontrado
        '''
        1. camino = self.pathfinder.EncontrarCamino(self.inicio, self.fin)
        
        2. SI camino es None:
            3. IMPRIMIR "No existe camino"
            4. RETORNAR
        
        5. IMPRIMIR "Camino encontrado con", longitud(camino), "pasos"
        6. self.pathfinder.VisualizarCamino(camino)
"""