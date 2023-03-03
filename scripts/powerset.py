# Recursive power set implementation
def power_set(S: set) -> list:
    """ 
        Return the power set of a set S.
        The power set of a set is the set of all its subsets.

        Pre: S is a set. 
        Post: Return the power set of S.
    """

    s_ = set(S).copy()
    a = s_.pop()

    T = power_set(s_) if s_ else [[]]

    return T + [t + [a] for t in T]

# recursive list of lists to frozenset of frozensets

def list_to_set(L: list) -> frozenset:
    """ 
        Return a frozenset of frozensets from a list of lists.
        The frozensets are the elements of the list.

        Pre: L is a list of lists. 
        Post: Return a frozenset of frozensets from L.
    """

    if L:
        return frozenset([frozenset(L.pop())] + list(list_to_set(L)))
    else:
        return frozenset()


if __name__ == '__main__':

    S = [1, 2, 3]
    R = power_set(S)
    print(R)

    print(list_to_set(R))
