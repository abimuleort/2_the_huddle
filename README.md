# Restructured Map POO

Refactorización orientada a objetos del proyecto [`interactive_map`](https://github.com/abimuleort/interactive_map): un mapa de cuadrícula con obstáculos y búsqueda de la ruta más corta mediante el algoritmo de Dijkstra, ahora estructurado en clases.

## Descripción

La versión original (procedural) se reorganizó usando **Programación Orientada a Objetos**, separando responsabilidades en dos clases principales:

- **`Mapa`**: representa la cuadrícula, gestiona las coordenadas de inicio (`I`) y fin (`S`), la colocación segura de obstáculos y la visualización del mapa en consola.
- **`BuscadorDeRutas`**: encapsula la lógica de pathfinding (Dijkstra), calculando si existe un camino entre dos puntos, reconstruyéndolo y marcándolo sobre el mapa.

El objetivo del proyecto es practicar diseño POO, separación de responsabilidades entre "modelo del mapa" y "algoritmo de búsqueda", y colocación de obstáculos que no bloqueen por completo el camino entre el inicio y el destino.

## Funcionalidades

- Creación de un mapa de tamaño configurable, con inicio y fin definidos por el usuario.
- Colocación de obstáculos (agua `~` y edificios `X`) verificando en cada intento que siga existiendo un camino válido entre inicio y fin.
- Búsqueda de la ruta de menor costo con Dijkstra (vía `heapq`).
- Reconstrucción y visualización del camino encontrado sobre el mapa.

## Estructura del proyecto

```
restructured_map_poo/
├── mapa_interactivo_oop_2.py   # Versión POO principal: clases Mapa y BuscadorDeRutas
├── mapa_interactivo_oop.py     # Versión previa de la refactorización POO
├── int_map_poo_2.py            # Iteración / variante del ejercicio
└── pseudo.py                   # Pseudocódigo de planificación del diseño
```

## Tecnologías

- Python 3
- `heapq` (Dijkstra)
- `math`, `random`, `copy`

## Instalación y uso

```bash
git clone https://github.com/abimuleort/restructured_map_poo.git
cd restructured_map_poo
python mapa_interactivo_oop_2.py
```

El programa solicitará por consola:
1. Cantidad de filas y columnas del mapa.
2. Coordenadas de inicio y destino.
3. Cantidad de obstáculos de agua y de edificios a colocar.

Luego mostrará el mapa con los obstáculos colocados y, si existe, el camino óptimo encontrado.

## Notas

Proyecto de práctica enfocado en aplicar POO sobre un ejercicio de pathfinding ya resuelto de forma procedural, mejorando la organización del código y la mantenibilidad de la lógica de búsqueda de caminos.
