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
    
    def AgregarObstaculos(self):
        if not (self.inicio and self.fin):
            print("Error: Define inicio y fin para comenzar")
            return False
    
        cantidad_agua = int(input("Ingrese la cantidad de obstagulos (Agua) desea agregar:  "))
        cantidad_edificio = int(input("Ingrese la cantidad de obstagulos (Edificio) desea agregar:  "))
        total_obstaculos = cantidad_agua + cantidad_edificio
        celdas_disponibles = (self.filas * self.columnas) -2

        if total_obstaculos >= celdas_disponibles:
            print("Demasiados obstaculos para las dimensiones del mapa")
            return False
        
        for i in range (cantidad_agua -1):
            if not self.ColocarObstaculoSeguro("~"):
                print("No se pudo colocar obstaculo: Agua")
                break
        
        for i in range (cantidad_edificio -1):
            if not self.ColocarObstaculoSeguro("X"):
                print("No se pudo colocar obstaculo: Edidicio")
                break
        return True
        
    def ColocarObstaculoSeguro(self, simbolo):




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