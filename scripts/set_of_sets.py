from typing import Set, FrozenSet


def set_of_set_of_set(s: Set[int]) -> FrozenSet[FrozenSet[FrozenSet[int]]]:
    
    if len(s) == 0:
        return frozenset()

    first : int = s.pop()
    if len(s) == 0:
        print("first: ", first)
        return frozenset({ frozenset({ frozenset({first}) }) })
    
    sub : FrozenSet[FrozenSet[FrozenSet[int]]] = set_of_set_of_set(s)
    print("sub: ", sub)
    res : FrozenSet[FrozenSet[FrozenSet[int]]] = frozenset({ frozenset({ frozenset({first}) }) }) | sub
    for x in sub:
        print("x: ", x)
        print("first: ", first)
        print("frozenset({first} | x): ", frozenset({first} | x))
        print("frozenset({ frozenset({first} | x) }): ", frozenset({ frozenset({first} | x) }))
        print("frozenset({ frozenset({first} | x) }) | set_of_set_of_set(s): ", frozenset({ frozenset({first} | x) }) | set_of_set_of_set(s))
        #return frozenset({ frozenset({first} | x) }) | set_of_set_of_set(s)
        res = res | frozenset({ frozenset({first} | x) })
    return res
    #return frozenset({ frozenset({first} | x) for x in set_of_set_of_set(s) })
    
def print_frozen_set_recursive(s: FrozenSet[FrozenSet[FrozenSet[int]]], indent: int = 0):
    
    print("{")

    for x in s:
        print("    " * indent, end="")
        if isinstance(x, frozenset):
            print_frozen_set_recursive(x, indent + 1)
        else:
            print(x)

    print("    " * (indent-1) + "}")
    s
if __name__ == "__main__":
    print_frozen_set_recursive(set_of_set_of_set({1,2,3}))
