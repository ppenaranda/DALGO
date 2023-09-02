import sys
def pancake(arreglo):
    n = len(arreglo)
    flips = []
    for i in range(n - 1, 0, -1):
        i_max = arreglo.index(max(arreglo[:i + 1]))
        
        if i_max != i:
            if i_max != 0:
                arreglo[:i_max + 1] = reversed(arreglo[:i_max + 1])
                flips.append(i_max + 1)  
            arreglo[:i + 1] = reversed(arreglo[:i + 1])
            flips.append(i + 1)  

    if flips == []:
        flips = "ORDENADO"
    else:
        flips = [x - 1 for x in flips]

    return flips

def main():
    linea = sys.stdin.readline().strip()
    ncasos = int(linea)
    for i in range(ncasos):
        linea = sys.stdin.readline().strip()
        numeros = [int(num) for num in linea.split()]
        respuesta = pancake(numeros)
        if respuesta != "ORDENADO":
            prt = [str(elemento) for elemento in respuesta]
            resultado = ' '.join(prt)
            print(resultado)
            linea = sys.stdin.readline()
        else:
            print(respuesta)
            linea = sys.stdin.readline()
main()