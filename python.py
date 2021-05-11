import subprocess

def __main__():
    finalizado = False
    posible = True

    nombreArchivo = input("Ingrese el nombre del archivo a leer sin el '.txt': ")

    while (not finalizado) and posible:

        response = subprocess.run("./a.exe " + nombreArchivo + ".txt")

        if response == 0:
            posible = False
            
            print("El archivo " + nombreArchivo + ".txt tenia posiciones repetidas o sus valores no entaban dentro de las dimensiones")
        else:
            archivo = open("laberinto.txt", 'r')

            valores, final, posInicial = obtenerValores(archivo)   

            aVisitar = [posInicial]
            
            diccionario = {}
            diccionario[posInicial] = posInicial
            diccionario = resolverLaberinto(aVisitar, diccionario, final, valores)

            recorrido = []

            aBuscar = final

            if final in diccionario:
                finalizado = True
                
                while aBuscar != posInicial:
                    recorrido.append(aBuscar)

                    aBuscar = diccionario[aBuscar]

                recorrido.append(posInicial)

                recorrido.reverse()

                print(recorrido)
            else:
                print("De nuevo")

def obtenerValores(archivo):
    lineas = archivo.readlines()

    valores = []
    final = []
    posInicial = []

    fila = 1
    for linea in lineas:
        if linea.count('X') > 0:
            final = [fila, linea.index('X') + 1]

        if linea.count('I') > 0:
            posInicial = [fila, linea.index('I') + 1]

        valores.append(list(linea))
        valores[fila-1].pop(len(valores[fila-1])-1)

        fila += 1
    
    return valores, (final[0], final[1]), (posInicial[0], posInicial[1])

def resolverLaberinto(aVisitar, diccionario, final, valores):
    actual = aVisitar[0]

    while (len(aVisitar) != 0) and (valores[actual[0] - 1][actual[1] - 1] != 'X') :
        actual = aVisitar[0]
        (y, x) = actual

        aVisitar, diccionario = inspeccionar(actual, y, x-1, aVisitar, diccionario, valores)
        aVisitar, diccionario = inspeccionar(actual, y, x+1, aVisitar, diccionario, valores)
        aVisitar, diccionario = inspeccionar(actual, y-1, x, aVisitar, diccionario, valores)
        aVisitar, diccionario = inspeccionar(actual, y+1, x, aVisitar, diccionario, valores)

        aVisitar.pop(0)

    return diccionario

def inspeccionar(actual, y, x, aVisitar, diccionario, valores):
    if (x > 0) and (x <= len(valores)) and (y > 0) and (y <= len(valores)) and (valores[y - 1][x - 1] != '1') and (not (y, x) in diccionario) and (not (y, x) in aVisitar):
        aVisitar.append((y, x))

        diccionario[(y, x)] = actual

    return aVisitar, diccionario

__main__()