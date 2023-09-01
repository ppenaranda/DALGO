import sys
def pancake(arreglo):
    n = len(arreglo)
    flips = []
    for i in range(n -1, 0, -1):
        i_mayor = arreglo.index(max(arreglo[:i+1]))
        if i_mayor != i:
            arreglo[:i_mayor + 1] = reversed(arreglo[:i_mayor+1])
            flips.append(i_mayor + 1)
            arreglo[:i+1] = reversed(arreglo[:i+1])
            flips.append(i)
    if flips == []:
        flips = "ORDENADO"
    
    return flips

def main():
    linea = sys.stdin.readline().strip()
    ncasos = int(linea)
    for i in range(ncasos):
        linea = sys.stdin.readline().strip()
        numeros = [int(num) for num in linea.split()]
        respuesta = pancake(numeros)
        print(str(respuesta))
        linea = sys.stdin.readline()


main()