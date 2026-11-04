
def calculadora(op, n1, n2):
    match op:
        case 1:
            return multiplicacao(n1, n2)
        case 2:
            return soma(n1, n2)
        case 3:
            return sub(n1, n2)
        


def multiplicacao(n1, n2):
    return n1 * n2

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2
