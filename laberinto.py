def TomarEntrada():
    ArchivoEntrada = input("Ingrese el nombre del archivo a leer: ")
    Entrada = open(ArchivoEntrada,"r")
    Laberinto = []
    Piso = []
    Lineas = Entrada.readlines()
    Entrada.close()
    Inicio = (0,0)
    i = 1
    j = 1
    for l in Lineas:
        Fila = list(l)
        Fila.pop()
        Laberinto.append(Fila)
        for Character in Fila :
            if(Character != '\n'): 
                if(Character == 'I'):
                    Inicio = (i,j) 
            j = j + 1
        i = i + 1
        j = 1
        Piso.clear()
    return Laberinto, Inicio
def Proceso():
    Laberinto = []
    Laberinto , Inicio = TomarEntrada()
    Inicio = (Inicio[0]-1, Inicio[1]-1)
    Maximos = (7,7)
    RecorridoFinal = []
    RecorridoFinal = Recorrido(Laberinto, Inicio, RecorridoFinal, Maximos)
    RecorridoFinal.reverse()



def Recorrido(Laberinto, Inicio, RecorridoFinal, Maximos):
    if(Laberinto[Inicio[0]][Inicio[1]] == "X"):
        RecorridoFinal.append(Inicio)
        return RecorridoFinal
    elif((Inicio[1]+ 1) < Maximos[1] and Laberinto[Inicio[0]][Inicio[1]+1] == "0" ):  #mueve a derecha
        print(Inicio)
        Inicio = (Inicio[0], Inicio[1]+1) 
        Recorrido(Laberinto, Inicio, RecorridoFinal, Maximos)
        Inicio = (Inicio[0], Inicio[1]-1)
        RecorridoFinal.append(Inicio)
    elif((Inicio[0]+ 1) < Maximos[0] and Laberinto[Inicio[0]+1][Inicio[1]] == "0" ):  #mueve a abajo
        Inicio = (Inicio[0]+1, Inicio[1])
        Recorrido(Laberinto, Inicio, RecorridoFinal, Maximos)
        Inicio = (Inicio[0], Inicio[1]-1)
        RecorridoFinal.append(Inicio)
    elif ((Inicio[1]- 1 < -1) and Laberinto[Inicio[0]][Inicio[1]-1] == "0") :  #mueve a izquierda
        Inicio = (Inicio[0], Inicio[1]-1)
        Recorrido(Laberinto, Inicio, RecorridoFinal, Maximos)
        RecorridoFinal.append(Inicio)
    elif((Inicio[0]- 1 < -1) and (Laberinto[Inicio[0]][Inicio[1]-1] == "0")) :  #mueve a arriva
        Inicio = (Inicio[0]-1, Inicio[1])
        Recorrido(Laberinto, Inicio, RecorridoFinal, Maximos)
        Inicio = (Inicio[0], Inicio[1]-1)
        RecorridoFinal.append(Inicio)
    return RecorridoFinal




if __name__ == "__main__":
   Proceso()
