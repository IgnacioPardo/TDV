
""" 
Una empresa utiliza una flota de camiones para realizar el reparto de su mercadería. Antes de cada viaje, se debe decidir qué paquetes de mercadería cargar en cada camión, de modo de aprovechar los viajes al máximo. Cada camión tiene una capacidad máxima de m metros cúbicos, y cada paquete a transportar tiene un volumen (en metros cúbicos). El problema de bin packing consiste en determinar en qué camión se ubica cada paquete, de modo tal de utilizar la menor cantidad de camiones. Escribir un algoritmo de backtracking para este problema. 
"""

from typing import List, Set

recursive_calls = 0

best_k = float('inf')

def binpacking(paquetes: List[int], capacidad: int, solucion_parcial: List[int]) -> List[int]:
    
    # if len(solucion_parcial) < 5:
    #     print(f"paquetes: {paquetes}, capacidad: {capacidad}, solucion_parcial: {solucion_parcial}")

    global recursive_calls
    recursive_calls += 1
    #print(f"recursive_calls: {recursive_calls}")

    global best_k

    #print(f"best k: {best_k}")

    if len(paquetes) == 0:
        return solucion_parcial
    
    solucion : List[int] = solucion_parcial.copy()

    ops = []
    pack = paquetes[0]
    if pack <= capacidad:
        # Sacar el paquete actual de la lista de paquetes
        n_paquetes = paquetes.copy()[1:]

        # Por cada camion que ya tenga paquetes cargados (solucion_parcial), agregar el paquete actual a cada uno de ellos
        for i in range(len(solucion_parcial)):
            # Poda por factibilidad, si el paquete actual no cabe en el camion i, no lo agrego
            # Poda por optimalidad, si la cantidad de camiones que tengo hasta ahora es menor a la mejor solucion encontrada, no sigo
            if solucion_parcial[i] + pack <= capacidad and len(solucion) < best_k:
                n_s_parcial = solucion_parcial.copy()
                n_s_parcial[i] += pack

                # Me guardo todas las posibles soluciones
                ops.append(binpacking(n_paquetes, capacidad, n_s_parcial))

        # Crear un nuevo camion con el paquete actual
        # La poda por optimalidad no se aplica aca, porque no estoy agregando el paquete a un camion existente, sino a uno nuevo, por lo que no estoy aumentando la cantidad de camiones
        n_s_parcial = solucion_parcial.copy()
        n_s_parcial.append(pack)
        op1 = binpacking(n_paquetes, capacidad, n_s_parcial)
        ops.append(op1)

    # La solucion es la que tenga menos camiones
    solucion = min(ops, key=len)

    # Actualizo el mejor k
    if len(solucion) < best_k:
        best_k = len(solucion)
        print(f"solucion: {solucion}, k: {best_k}")

    return solucion

if __name__ == "__main__":
    paquetes : List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    capacidad : int = 10
    # Solucion: cantidad de camiones utilizados
    solucion_actual : List[int] = []
    solucion = binpacking(paquetes, capacidad, solucion_actual)
    print(f"Solucion: {solucion}")
