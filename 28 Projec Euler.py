import math
CantidadFilasyColumnas = 1001   ###Debe ser un numero impar
filas = CantidadFilasyColumnas
Columnas = CantidadFilasyColumnas 
inicialfilas= 0
inicialcolum = Columnas-1
numeros = filas*Columnas
datos = [[0 for _ in range(Columnas)] for _ in range(filas)]
mitad = math.ceil(len(datos)/2)
######################################################################## 
def VerificacionVacios(Giro,Posicion,a,b) : 
## arriba = 8 / abajo = 2 / izquierda = 4 / derecha = 6

################## a = fila ########## b = columna ###########
    if Giro == 4:  # izquierda
        if b - 1 >= 0 and Posicion[a][b - 1] == 0:
            return True
    if Giro == 6:  # derecha
        if b + 1 < len(Posicion[0]) and Posicion[a][b + 1] == 0:
            return True

    if Giro == 2:  # abajo
        if a + 1 < len(Posicion) and Posicion[a + 1][b] == 0:
            return True

    if Giro == 8:  # arriba
        if a - 1 >= 0 and Posicion[a - 1][b] == 0:
            return True
    return False 
 #######################################################################   

while datos[mitad][mitad] == 0: 
    while VerificacionVacios(4,datos,inicialfilas,inicialcolum) :
        datos[inicialfilas][inicialcolum] = numeros
        numeros -= 1
        inicialcolum -=1
    while VerificacionVacios(2,datos,inicialfilas,inicialcolum) :
        datos[inicialfilas][inicialcolum] = numeros
        numeros -= 1
        inicialfilas +=1
    while VerificacionVacios(6,datos,inicialfilas,inicialcolum) :
        datos[inicialfilas][inicialcolum] = numeros
        numeros -= 1
        inicialcolum +=1
    while VerificacionVacios(8,datos,inicialfilas,inicialcolum) :
        datos[inicialfilas][inicialcolum] = numeros
        numeros -= 1
        inicialfilas -=1

datos[mitad-1][mitad] = 2 ## correciones de logica
datos[mitad-1][mitad-1] = 1 ## correciones de logica
###encontrar la suma de cualquier matriz impar #######
suma1 = 0
suma2 = 0
control2 = CantidadFilasyColumnas-1
for a in range (0, CantidadFilasyColumnas) : 
    suma1 = datos[a][a] + suma1
    suma2 = datos[a][control2] + suma2
    control2 -=1
print(suma1+suma2-1) 