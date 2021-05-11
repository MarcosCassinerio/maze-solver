#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define largoLinea 25

int crearLaberinto(int largoNombre, char nombreArchivo[largoNombre]) {
    FILE *archivo;
    archivo = fopen(nombreArchivo, "r");

    int dimensiones, cantidadParedes, repetido = 0, inicialX, inicialY, objetivoX, objetivoY, obstaculoX, obstaculoY;

    fscanf(archivo, "dimension\n%d\nobstaculos fijos\n", &dimensiones);

    char *valores[dimensiones];

    for (int i = 0 ; i < dimensiones ; ++i) {
        valores[i] = (char *)malloc((dimensiones - 1) * sizeof(char *));

        valores[0][i] = '0';
    }

    for (int i = 1 ; i < dimensiones ; ++i) {
        strcpy(valores[i], valores[0]);
    }

    while(fscanf(archivo, "(%d,%d)\n", &obstaculoY, &obstaculoX) && repetido == 0) {
        if ((obstaculoY < 0) || (obstaculoY > (dimensiones-1)) || (obstaculoX < 0) || (obstaculoX > (dimensiones-1)) || valores[obstaculoY-1][obstaculoX-1] == '1') {
            repetido = 1;
        } else {
            valores[obstaculoY-1][obstaculoX-1] = '1';
        }
    }

    if (repetido == 0) {
        fscanf(archivo, "obstaculos aleatorios\n%d\n", &cantidadParedes);

        fscanf(archivo, "posicion inicial\n(%d,%d)\n", &inicialY, &inicialX);

        fscanf(archivo, "objetivo\n(%d,%d)\n", &objetivoY, &objetivoX);
    }

    fclose(archivo);

    if (repetido == 0) {
        if ((inicialY > 0) && (inicialY <= dimensiones) && (inicialX > 0) && (inicialX <= dimensiones) && valores[inicialY-1][inicialX-1] == '0') {
            valores[inicialY-1][inicialX-1] = 'I';
        } else {
            repetido = 1;
        }
    }

    if (repetido == 0) {
        if ((objetivoY > 0) && (objetivoY <= dimensiones) && (objetivoX > 0) && (objetivoX <= dimensiones) && valores[objetivoY-1][objetivoX-1] == '0') {
            valores[objetivoY-1][objetivoX-1] = 'X';
        } else {
            repetido = 1;
        }
    }
    

    if (repetido == 0) {
        FILE *laberinto;
        laberinto = fopen("laberinto.txt","w+");

        srand(time(NULL));
        for (int i = 0 ; i < cantidadParedes ; i++) {
            int rand1 = rand()%dimensiones, rand2 = rand()%dimensiones;
            if (valores[rand1][rand2] == '0') {
                valores[rand1][rand2] = '1';
            } else {
                i--;
            }
        }

        for (int i = 0 ; i < dimensiones ; i++) {
            valores[i][dimensiones] = '\0';
            fputs(valores[i], laberinto);
            fputc('\n', laberinto);
            free(valores[i]);
        }

        free(valores);

        fclose(laberinto);

        return 1;
    } else {
        for (int i = 0 ; i < dimensiones ; i++) {
            free(valores[i]);
        }

        free(valores);
        
        return 0;
    }
}

int main(int argc, char *argv[]) {

    int largoNombre = strlen(argv[1]);

    return crearLaberinto(largoNombre, argv[1]);
}