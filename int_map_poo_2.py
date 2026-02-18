import random
import math
import heapq
import copy

class Mapa:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.mapa = [["." for _ in range(columnas)] for _ in range(filas)]
        self.inicio = None
        self.fin = None
        self.buscador_de_rutas = BuscadorDeRutas(self)

    def Coordenadas(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
        fila_inicio, columna_inicio = inicio
        fila_fin, columna_fin = fin
        self.mapa[fila_inicio][columna_inicio] = "I"
        self.mapa[fila_fin][columna_fin] = "S"

    def MostrarMapa(self):
        for fila in self.mapa:
            print(" ".join(fila))
        print()  # línea extra para claridad

    def AgregarObstaculos(self):
        if self.inicio is None or self.fin is None:
            print("Error: Define inicio y fin para comenzar")
            return False

        cantidad_agua = int(input("Ingrese la cantidad de obstáculos (Agua) desea agregar: "))
        cantidad_edificio = int(input("Ingrese la cantidad de obstáculos (Edificio) desea agregar: "))
        total_obstaculos = cantidad_agua + cantidad_edificio
        celdas_disponibles = (self.filas * self.columnas) - 2

        if total_obstaculos >= celdas_disponibles:
            print("Demasiados obstáculos para las dimensiones del mapa")
            return False

        for _ in range(cantidad_agua):
            if not self.ColocarObstaculoSeguro("~"):
                print("No se pudo colocar obstáculo: Agua")
                break

        for _ in range(cantidad_edificio):
            if not self.ColocarObstaculoSeguro("X"):
                print("No se pudo colocar obstáculo: Edificio")
                break

        return True

    def ColocarObstaculoSeguro(self, simbolo):
        intentos = 0
        max_intentos = self.filas * self.columnas * 3

        while intentos < max_intentos:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)

            if self.CeldaEsValida(fila, columna):
                valor_anterior = self.mapa[fila][columna]
                self.mapa[fila][columna] = simbolo

                if self.buscador_de_rutas.ExisteCamino(self.inicio, self.fin):
                    return True
                else:
                    self.mapa[fila][columna] = valor_anterior
            intentos += 1

        return False

    def MostrarCaminoOptimo(self):
        camino = self.buscador_de_rutas.EncontrarCamino(self.inicio, self.fin)
        if camino is None:
            print("No hay caminos disponibles")
            return
        print(f"Camino encontrado con {len(camino)} pasos:")
        self.buscador_de_rutas.VisualizarCamino(camino)

    def CeldaEsValida(self, fila, columna):
        if not (0 <= fila < self.filas and 0 <= columna < self.columnas):
            return False
        if (fila, columna) == self.inicio or (fila, columna) == self.fin:
            return False
        if self.mapa[fila][columna] != ".":
            return False
        return True

    def ArregloIndices(self):
        print(" " + " ".join(str(c) for c in range(self.columnas)))
        for fila_index, fila in enumerate(self.mapa):
            print(f"{fila_index} " + " ".join(fila))

class BuscadorDeRutas:
    def __init__(self, mapa):
        self.mapa = mapa
        self.filas = mapa.filas
        self.columnas = mapa.columnas

    def ExisteCamino(self, inicio, fin):
        return self.EncontrarCamino(inicio, fin) is not None

    def EncontrarCamino(self, inicio, fin):
        if inicio is None or fin is None:
            return None

        dist = {(i, j): math.inf for i in range(self.filas) for j in range(self.columnas)}
        dist[inicio] = 0
        padre = {}
        visitados = set()
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (0, inicio))

        while cola_prioridad:
            distancia_actual, posicion_actual = heapq.heappop(cola_prioridad)
            if posicion_actual in visitados:
                continue
            visitados.add(posicion_actual)

            if posicion_actual == fin:
                return self.ReconstruirCamino(padre, inicio, fin)

            for vecino in self.ObtenerVecinosTransitables(posicion_actual):
                nueva_distancia = distancia_actual + 1
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
            nf, nc = fila + df, columna + dc
            if 0 <= nf < self.filas and 0 <= nc < self.columnas:
                celda = self.mapa.mapa[nf][nc]
                if celda in (".", "I", "S"):
                    vecinos.append((nf, nc))
        return vecinos

    def ReconstruirCamino(self, padre, inicio, fin):
        camino = []
        actual = fin
        while actual != inicio:
            camino.append(actual)
            actual = padre.get(actual)
            if actual is None:
                return None
        camino.append(inicio)
        camino.reverse()
        return camino

    def VisualizarCamino(self, camino):
        mapa_copia = copy.deepcopy(self.mapa.mapa)
        for fila, columna in camino:
            if mapa_copia[fila][columna] not in ("I", "S"):
                mapa_copia[fila][columna] = "*"
        for fila in mapa_copia:
            print(" ".join(fila))
        print()


def main():
    print("-- Buscador de Rutas --\n")
    filas = int(input("Cantidad de filas del mapa: "))
    columnas = int(input("Cantidad de columnas del mapa: "))
    mapa = Mapa(filas, columnas)
    mapa.ArregloIndices()

    fila_i = int(input("Ingrese la fila de inicio: "))
    col_i = int(input("Ingrese la columna de inicio: "))
    fila_f = int(input("Ingrese la fila de destino: "))
    col_f = int(input("Ingrese la columna de destino: "))
    inicio = (fila_i, col_i)
    fin = (fila_f, col_f)
    mapa.Coordenadas(inicio, fin)
    mapa.ArregloIndices()

    if mapa.AgregarObstaculos():
        print("Mapa con obstáculos:")
        mapa.ArregloIndices()

    mapa.MostrarCaminoOptimo()


if __name__ == "__main__":
    main()
