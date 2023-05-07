"""
13. Tenemos cajas numeradas de 1 a N, todas de iguales dimensiones. Queremos encontrar la máxima cantidad de cajas que pueden apilarse en una única pila cumpliendo que:
sólo puede haber una caja apoyada directamente sobre otra;
las cajas de la pila deben estar ordenadas crecientemente por número, de abajo para arriba;
cada caja i tiene un peso wi y un soporte si, y el peso total de las cajas que están arriba de otra no debe exceder el soporte de esa otra.
3
Si tenemos los pesos w = [19,7,5,6,1] y los soportes s = [15,13,7,8,2] (la caja 1 tiene peso 19 y soporte 15, la caja 2 tiene peso 7 y soporte 13, etc.), entonces la respuesta es 4. Por ejemplo, pueden apilarse de la forma 1-2-3-5 o 1-2-4-5 (donde la izquierda es más abajo), entre otras opciones.
a) Pensar la idea de un algoritmo de backtracking (no hace falta escribirlo).
b) Escribir una formulación recursiva que sea la base de un algoritmo de PD. Explicar su
semántica e indicar cuáles serían los parámetros para resolver el problema.
c) Diseñar un algoritmo de PD y dar su complejidad temporal y espacial auxiliar.
Comparar cómo resultaría un enfoque top-down con uno bottom-up.
"""

from pprint import pprint
from typing import List, Tuple
from random import shuffle

ops = []


def cajas(c: List[int], w: List[int], s: List[int]) -> Tuple[List[int], int]:

    n: int = len(c)
    best_sol = c.copy()

    for nueva_caja in list(set(range(len(w))) - set(c)):

        skip = False
        for caja_agregada in c:
            if s[caja_agregada] < w[nueva_caja]:
                skip = True
                break

        if not skip:

            s_aux = s.copy()

            for caja_agregada in c:
                s_aux[caja_agregada] -= w[nueva_caja]

            nuevo_c = c.copy()
            nuevo_c.append(nueva_caja)

            """ Poda por optimalidad
            cajas_restantes = list(set(range(len(w))) - set(nuevo_c))
            max_pesos = sum([w[i] for i in cajas_restantes])
            min_soporte = min([s[i] for i in nuevo_c])

            if len(cajas_restantes) + len(nuevo_c) > n:
                if max_pesos <= min_soporte: """

            sol, n_sol = cajas(nuevo_c, w, s_aux)
            n = max(n, n_sol)

            best_sol = sol if n_sol > len(best_sol) else best_sol

    return best_sol, len(best_sol)


def cajas_alt(c: List[int], w: List[int], s: List[int]) -> Tuple[List[int], int]:

    n: int = len(c)
    best_sol = c.copy()

    for nueva_caja in list(set(range(len(w))) - set(c)):

        s_aux = s.copy()

        skip = False
        for caja_agregada in c:
            s_aux[caja_agregada] -= w[nueva_caja]
            if s_aux[caja_agregada] < w[nueva_caja]:
                skip = True
                break

        if not skip:

            nuevo_c = c.copy()
            nuevo_c.append(nueva_caja)

            sol, n_sol = cajas_alt(nuevo_c, w, s)
            n = max(n, n_sol)

            best_sol = sol if n_sol > len(best_sol) else best_sol

    return best_sol, len(best_sol)


def cajas_pd(
        c: List[int],
        w: List[int],
        s: List[int],
        memo: List[List[int]]
) -> Tuple[List[int], int]:

    # Memo contiene en la fila j columna i, la mejor solución para cuando el item j está en c en la posición i

    for caja_pos, caja in enumerate(c):
        if memo[caja][caja_pos] != -1:
            return c, memo[caja][caja_pos]

    n: int = len(c)
    best_sol = c.copy()

    for nueva_caja in list(set(range(len(w))) - set(c)):

        s_aux = s.copy()

        skip = False
        for caja_agregada in c:
            s_aux[caja_agregada] -= w[nueva_caja]
            if s_aux[caja_agregada] < w[nueva_caja]:
                skip = True
                break

        if not skip:

            nuevo_c = c.copy()
            nuevo_c.append(nueva_caja)

            sol, n_sol = cajas_pd(nuevo_c, w, s, memo)
            n = max(n, n_sol)

            best_sol = sol if n_sol > len(best_sol) else best_sol

            for caja_pos, caja in enumerate(nuevo_c):
                memo[caja][caja_pos] = n_sol

    return best_sol, len(best_sol)


ids = [0, 1, 2, 3, 4]
w = [19, 7, 5, 6, 1]
s = [15, 13, 7, 8, 2]
c = []

boxes = list(zip(w, s, ids))

def check_greedy(w, s):
    print(cajas_alt([], w[:2], s[:2]))
    print(cajas_alt([], w[:3], s[:3]))
    print(cajas_alt([], w[:4], s[:4]))
    print(cajas_alt([], w, s))


print(boxes)

check_greedy(w, s)
print()
# Randomize order of boxes

""" shuffle(boxes)

w, s, ids = zip(*boxes)

w, s = list(w), list(s)

print(boxes)
check_greedy(w, s) """


# Memo contiene en la fila j columna i, la mejor solución para cuando el item j está en c en la posición i

memo = [[-1 for _ in range(len(w))] for _ in range(len(w))]

#print(cajas_pd([], w, s, memo))



# time execution of cajas_alt and cajas_pd

import timeit

# random boxes

from random import randint

w = [randint(1, 100) for _ in range(10)]
s = [randint(1, 100) for _ in range(10)]

memo = [[-1 for _ in range(len(w))] for _ in range(len(w))]
v_1 = timeit.timeit(lambda: cajas_alt([], w, s), number=1000)
v_2 = timeit.timeit(lambda: cajas_pd([], w, s, memo), number=1000)


print(w, s)
print(cajas_alt([], w, s))
pprint(memo)
print(v_1, v_2, v_1 / v_2)


[3, 90, 50, 33, 8, 78, 36, 40, 68, 82]
[86, 1, 89, 45, 30, 45, 41, 91, 33, 72]

([2, 0, 7, 3, 4], 5)

[[3, 4, -1, -1, -1, -1, -1, -1, -1, -1],
 [1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [4, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [2, 4, 4, -1, -1, -1, -1, -1, -1, -1],
 [2, 4, 4, 4, -1, -1, -1, -1, -1, -1],
 [2, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [2, 4, 4, -1, -1, -1, -1, -1, -1, -1],
 [2, 4, 4, -1, -1, -1, -1, -1, -1, -1],
 [2, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [2, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
