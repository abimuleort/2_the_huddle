# CLASE Mapa:
#     ATRIBUTOS:
#         - filas: entero
#         - columnas: entero
#         - matriz: arreglo 2D
#         - inicio: tupla (fila, columna)
#         - fin: tupla (fila, columna)
class Mapa():
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.mapa = [["." for _ in range (columnas)] for _ in range (filas)]
    
    def Coordenadas(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
        fila_inicio, columna_inicio = inicio
        fila_fin, columna_fin = fin
        self.mapa[fila_inicio][columna_inicio] = "I"
        self.mapa[fila_fin][columna_fin] = "S"
    
    def MostrarMapa(self):
        for filas in self.mapa:
            print(*filas)


        
    
#     MÉTODO __init__(filas, columnas, inicio, fin):
#         1. Asignar filas y columnas
#         2. Validar que inicio y fin estén dentro de los límites
#         3. Crear matriz vacía de tamaño filas x columnas
#         4. Inicializar todas las celdas con '.'
#         5. Marcar posición inicio con 'I'
#         6. Marcar posición fin con 'F'
    
#     MÉTODO mostrar_mapa():
#         1. PARA cada fila EN matriz:
#             2. Imprimir fila completa
    
#     MÉTODO validar_coordenadas(fila, columna):
#         1. SI fila >= 0 Y fila < filas Y columna >= 0 Y columna < columnas:
#             2. RETORNAR Verdadero
#         3. SINO:
#             4. RETORNAR Falso

# PROGRAMA PRINCIPAL:
#     1. Solicitar al usuario número de filas
#     2. Solicitar al usuario número de columnas
#     3. Solicitar coordenadas de inicio (fila, columna)
#     4. Solicitar coordenadas de fin (fila, columna)
#     5. Crear objeto Mapa con los datos ingresados
#     6. Mostrar el mapa en pantalla
def main():
    filas = int(input("Cantidad de filas del mapa: "))
    columnas = int(input("Cantidad de columnas del mapa: "))
    mapa = Mapa(filas, columnas)
    mapa.MostrarMapa()
    fila_i = int(input("Ingrese la fila de inicio: "))
    col_i = int(input("Ingrese la columna de inicio: "))
    fila_f = int(input("Ingrese la fila de destino: "))
    col_f = int(input("Ingrese la columna de destino: "))
    inicio = fila_i, col_i
    fin = fila_f, col_f
    mapa.Coordenadas(inicio, fin)
    mapa.MostrarMapa()
main()