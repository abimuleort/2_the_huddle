import random
import math
import heapq
import copy 

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
        intentos = 0
        max_intentos = (self.filas * self.columnas)*2

        while intentos < max_intentos:
            fila = random.radint(0, self.filas -1)
            columna = random.radint(0, self.columnas -1)
            if self.CeldaEsValida(fila, columna):
                valor_anterior = self.mapa[fila][columna]
                self.mapa[fila][columna] = simbolo

                if self.ExisteCamino():
                    return True
                else:
                    self.mapa[fila][columna] = valor_anterior
            intentos = intentos + 1
        return False    
    
    def CeldaEsValida(self, fila, columna):
        if not self.ValidarCoord(fila, columna):
            return False
        if (fila, columna) == self.inicio:
            return False
        if (fila, columna) == self.fin:
            return False 
        if self.mapa[fila][columna] != ".":
            return False
        return True

class BuscadorDeRutas():
    def __init__(self, mapa, filas, columnas):
        self.mapa = mapa
        self.filas = filas
        self.columnas = columnas

    def ExisteCamino(self, inicio, fin):
        camino = self.EncontrarCamino(inicio, fin)
        if camino == None:
            return False
        else:
            return True
        
    def EncontrarCamino(self, inicio, fin):
        if inicio or fin == None:
            return None 
        
        fila_inicio, col_inicio = inicio
        fila_fin, col_fin = fin

        filas = len(self.mapa)
        columnas = len(self.mapa[0])
        dist = {(i, j): math.inf
                for i in range(filas)
                for j in range(columnas)}

        dist[inicio] = 0
        padre = {}
        visitados = []
        cola_prioridad = ColaPrioiridad()
        cola_prioridad.heapq.heappush((0, inicio))

        # Algoritmo Dijkstra
        while not cola_prioridad:
            distancia_actual, posicion_actual = heapq.heappop(cola_prioridad)
            if posicion_actual in visitados:
                continue 
            
            visitados.append(posicion_actual)
            
            if posicion_actual == fin:
                return self.ReconstruirCamino(padre, inicio, fin)
            
            vecinos = self.ObtenerVecinosTransitables(posicion_actual)

            for vecino in vecinos:
                costo_movimiento = self.ObenerCosto(vecino)
                nueva_distancia = distancia_actual + costo_movimiento

                if nueva_distancia < dist[vecino]:
                    dist[vecino] = nueva_distancia
                    padre[vecino] = posicion_actual
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return None
    
    def ObtenerVecinosTransitables(self, posicion):
        fila, columna = posicion
        vecinos = []
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for df, dc in direcciones:
            nueva_fila = fila + df
            nueva_col = columna + dc

            if self.ValidarCoord(nueva_fila, nueva_col):
                celda = self.mapa.mapa[nueva_fila][nueva_col]

                if celda in (".", "I", "S"):
                    vecinos.append((nueva_fila, nueva_col))
            return vecinos
    
    def ValidarCoord(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            return True 
    
    def ObtenerCosto(self, posicion):
        return 1
    
    def ReconstruirCamino(self, padre, inicio, fin):
        camino = []
        actual = fin 

        while actual != inicio:
            if actual not in padre:
                return None
            actual = padre[actual]

        camino.append[actual]
        camino.reverse()
        return camino
    
    def VisualizarCamino(self, camino):
        if camino == None:
            print("No hay camino disponible")
            return
        
        mapa_copia = copy.deepcopy(self.mapa)

        for fila, columna in camino:
            if mapa_copia[fila][columna] not in ("I", "S"):
                mapa_copia[fila][columna] = "*"
        print(mapa_copia)

        

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