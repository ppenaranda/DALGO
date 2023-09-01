def pancake(arreglo):
    tamano = len(arreglo)
    flips = []

    for i in range(tamano):
        valor_max = max(arreglo[i:])
        i_max = arreglo.index(valor_max)
        arreglo[i:i_max + 1] = reversed(arreglo[i:i_max + 1])
        flips.append(i_max)

    return arreglo, flips

def pancake2(arreglo):
    tamano = len(arreglo)
    flips = []
    for i in range(tamano):
        valor_max = max(arreglo[:tamano - i])
        i_max = arreglo.index(valor_max) +1 
        arreglo[:i_max] = reversed(arreglo[:i_max])
        flips.append(i_max)

        arreglo[:tamano-i] = reversed(arreglo[:tamano-i])
        flips.append(tamano-i)
    arreglo = list(reversed(arreglo))
    return arreglo, flips

## 1 4 3 2 5 ##

print(pancake([1,4,3,2,5]))

print(pancake2([1,4,3,2,5]))