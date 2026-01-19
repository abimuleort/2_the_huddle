from typing import List, Tuple, Optional, Set
import heapq
from enum import Enum 

class TipoCelda(Enum):
    LIBRE = "."
    OBSTACULO = "#"
    INICIO = "I"
    FIN = "F"
    RUTA = "*"

class Coordenada:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __eq__(self, otra):
        return self.x == otra.x and self.y == otra.y
    def __hash__(self):
        return hash((self.x, self.y))
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def distancia_manhattan(self, otra: 'Coordenada') -> int:
        return abs(self.x - otra.x) + abs(self.y - otra.y)
    def obtener_vecinos(self, max_x:int, max_y: int) -> List['Coordenada']:
        vecinos = []
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in movimientos:
            nuevo_x, nuevo_y = self.x + dx, self.y + dy
            if 0 <= nuevo_x < max_x and 0 <= nuevo_y < max_y:
                vecinos.append(Coordenada(nuevo_x, nuevo_y))
        return vecinos

class Ruta:
    def __init__(self, coordenadas: List[Coordenada], costo_total: int):
        self.coordenadas = coordenadas
        self.costo_total = costo_total
        self.longitud = len(coordenadas)
    def __repr__(self):
        return f"Ruta de {self.longitud} pasos (costo: {self.costo_total})"
    def contiene(self, coord: Coordenada) -> bool:
        return coord in self.coordenadas
    def obtener_descripcion(self) -> str:
        inicio = self.coordenadas[0]
        fin = self.coordenadas[-1]

        return(
            "Ruta encontrada: \n"
            f"Longitud total: {self.longitud} pasos\n"
            f"Costo total: {self.costo_total}\n"
            f"Punto de inicio: {inicio}\n"
            f"Punto de llegada: {fin}"
        )
class Mapa:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.obstaculos = set()
        self.inicio = None
        self.fin = None
    def validar_coordenada(self, coord):
        x, y = coord
        return 0 <= x < self.ancho and 0 <= y < self.alto
    def configurar_puntos(self, inicio, fin):
        if self.validar_coordenada(inicio):
            self.inicio = inicio
        else:
            raise ValueError(f"Inicio {inicio} invalido")
        if self.validar_coordenada(fin):
            self.fin = fin
        else:
            raise ValueError(f"Fin {fin} invalido")
    def agregar_obstaculo(self, coord):
        if self.validar_coordenada(coord):
            if coord != self.inicio and coord != self.fin:
                self.obstaculos.add(coord)
                return True
        return False
    def es_accesible(self, coord):
        return (self.validar_coordenada(coord) and coord not in self.obstaculos)
    def mostrar(self, ruta: Optional[Ruta] = None):
        print("\n" + "=" *(self.ancho * 2 + 1))
        for y in range(self.alto):
            fila = ""
            for x in range(self.ancho):
                coord = Coordenada(x, y)
                if coord == self._inicio:
                    fila += TipoCelda.INICIO.VALUE + " "
                elif coord == self._fin:
                    fila += TipoCelda.FIN.value + " "
                elif ruta and ruta.contiene(coord): 
                    fila += TipoCelda.RUTA.value + " "
                elif coord in self._obstaculos:
                    fila += TipoCelda.OBSTACULO.value + " "
                else:
                    fila += TipoCelda.LIBRE.value + " "
            print(fila)
        print("=" * (self.ancho *2 + 1))
        print(f"LEyenda: {TipoCelda.INICIO.value}=Inicio  "
        f"{TipoCelda.FIN.value}=Fin  "
        f"{TipoCelda.RUTA.value}=Ruta  "
        f"{TipoCelda.OBSTACULO.value}=Obstaculo\n")
class AlgoritmoBusqueda:
    def __init__(self, mapa: Mapa):
        self.mapa = mapa
    def encontrar_ruta(self, inicio: Coordenada, fin: Coordenada) -> Optional[Ruta]:
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
class DijkstraAlgoritmo(AlgoritmoBusqueda):
    def econtrar_ruta(self, inicio: Coordenada, fin: Coordenada) -> Optional[Ruta]:
        distancias = {inicio: 0}
        padres = {inicio: None}
        visitados = set()
        cola_prioridad = [(0, inicio)]
        while cola_prioridad:
            distancia_actual, actual = heapq.heappop(cola_prioridad)
            if actual in visitados:
                continue
            visitados.add(actual)
            if actual == fin:
                return self._reconstruir_ruta(padres, inicio, fin, distancia_actual)
            for vecino in actual.obtener_vecinos(self.mapa.ancho, self.mapa.alto):
                if not self.mapa.es_accesible(vecino) or vecino in visitados:
                    continue
                nueva_distancia = distancia_actual + 1
                if (
                    vecino not in distancias
                    or nueva_distancia < distancias[vecino]
                ):
                    distancias[vecino] = nueva_distancia
                    padres[vecino] = actual
                    heapq.heappush(
                        cola_prioridad, (nueva_distancia, vecino)
                    ) 
        return None
    def _reconstruir_ruta(self, padres: dict, inicio: Coordenada, fin: Coordenada, costo: int) -> Ruta:
        ruta = []
        actual = fin
        while actual is not None:
            ruta.append(actual)
            actual = padres[actual]
        ruta.reverse()
        return Ruta(ruta, costo)
class CalculadoraDeRutas:
    def __init__(self, mapa: Mapa, algoritmo: AlgoritmoBusqueda):
        self.mapa = mapa
        self.algoritmo = algoritmo
        self.ultima_ruta: Optional[Ruta] = None
    def calcular_ruta_corta(self) -> Optional[Ruta]:
        if not self.mapa.inicio or not self.mapa.fin:
            print("Falta definir el inicio o el destino")
            return None
        if not self.mapa.es_accesible(self.mapa.fin):
            print("E; punto de destino no es accesible")
            return None
        print("Buscando la mejor ruta...")
        self.ultima_ruta = self.algoritmo.encontrar_ruta(
            self.mapa.inicio, self.mapa.fin
        )
        return self.ultima_ruta
    def mostrar_resultado(self):
        if self.ultima_ruta:
            print("Ruta encontrada")
            print(self.ultima_ruta.obtener_descripcion())
            self.mapa_mostrar(self.ultima_ruta)
        else:
            print("No fue posible encontrar un camino")
            self.mapa_mostrar()
    def cambiar_algoritmo(self, nuevo_algoritmo: AlgoritmoBusqueda):
        self.algoritmo = nuevo_algoritmo
class InterfazUsuario:
    def __init__(self):
        self.mapa: Optional[Mapa] = None
        self.calculadora: Optional[CalculadoraDeRutas] = None
    def iniciar(self):
        print("=" * 60)
        print("Sistema de busqueda de rutas")
        print("=" * 60)
        self._configurar_mapa()
        self._configurar_obstaculosO()
        self._ejecutar_busqueda()
    def _configurar_mapa(self):
        ancho = self._solicitar_entero("Ingrese el ancho del mapa", minimo = 2, maximo = 50)
        alto = self._solicitar_entero("Ingrese el alto del mapa", minimo = 2, maximo = 50)
        self.mapa = Mapa(ancho, alto)
        algoritmo = DijkstraAlgoritmo(self.mapa)
        self.calculadora = CalculadoraDeRutas(self.mapa, algoritmo)
        print(f"MApa creado de forma exitosa ({ancho} x {alto})")
    def _configurar_obstaculos(self):
        cantidad = self._solicitar_entero("Cuantos obstaculos desea agregar?", minimo = 0, maximo = self.mapa.ancho * self.mapa.alto - 2)
        for i in range(cantidad):
            print(f"\nObstaculo {i+1}")
            x = self._solicitar_entero(' Coordenada X', 0, self.mapa.ancho - 1)
            y = self._solicitar_entero(' Coordenada', 0, self.mapa.alto - 1)
            if self.mapa.agregar_obstaculo(Coordenada(x, y)):
                continue
            else:
                print("Coordenada incorrecta, no se pudo agregar el obstaculo")
    def _ejecutar_busqueda(self):
        while True:
            print('\n' + "-" * 60)
            print("Busqueda de Rutas")
            print("\n Punto de inicio:")
            inicio_x = self._solicitar_entero(' Coordenada X', 0, self.mapa.ancho - 1)
            inicio_y = self._solicitar_entero(' Coordenada Y', 0, self.mapa.ancho - 1)
            self.mapa.inicio = Coordenada(inicio_x, inicio_y)

            print("\n Punto de destino: ")
            fin_x = self._solicitar_entero(' Coordenada X', 0, self.mapa.ancho - 1)
            fin_y = self._solicitar_entero(' Coordenada Y', 0, self.mapa.ancho - 1)
            self.mapa.fin = Coordenada(fin_x, fin_y)

            self.calculadora.calcular_ruta_corta()
            self.calculadora.mostrar_resultado()

            if not self._confirmar("\n Desea buscar otra ruta?"):
                break
    def _solicitar_entero(self, mensaje: str, minimo: int, maximo: int) -> int:
        while True:
            try:
                valor = int(input(f"{mensaje} ({minimo} -- {maximo}): "))
                if minimo <= valor <= maximo:
                    return valor
                print(f"Valor invalido, debe estar entre {minimo} y {maximo}")
            except ValueError:
                print("Ingrese un numero valido")
    def _confirmar(self, mensaje: str) -> bool:
        while True:
            respuesta = input(f"{mensaje} (s/n): ").lower().strip()
            if respuesta in ['s', 'si', 'sí', 'yes', 'y']:
                return True
            elif respuesta in ['n', 'no']:
                return False
            print("responda s/n")

if __name__ == "__main__":
    try:
        app = InterfazUsuario()
        app.iniciar()
    except KeyboardInterrupt:
        print("\n Ejecucion interrumpida por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")