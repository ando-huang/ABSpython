def even_filter(n1, n2, n3, n4):
    evens = [n1, n2, n3, n4]
    for elem in evens:
        if elem%2 != 0:
            evens.remove(elem)
    return evens
