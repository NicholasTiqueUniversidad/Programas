Año_base = 1900
Año_inicial = 1901
Año_Final = 2000

def Domingos (Año1,Año2): 
    ContadorDomingos = 0
    Meses = [["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
         [31,28,31,30,31,30,31,31,30,31,30,31]]
    Dias = ["lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
    dia="Hola"
    contador = 0
    for año in range(Año1,Año2+1):
        if año % 100 == 0 : 
            if año % 400 == 0 :
                Meses[1][1] = 29
            else :
                Meses[1][1] = 28    
        elif año % 4 == 0 :
            Meses[1][1] = 29 
        else : 
            Meses[1][1] = 28
        for q in range (0,12) :  
            for b in range (0,Meses[1][q]) :
                dia = Dias[contador]  
                contador = contador+1
                if dia == "Domingo" and b == 0 :
                  ContadorDomingos = ContadorDomingos + 1
                if contador == 7 :
                  contador = 0  
    return ContadorDomingos
Cuenta =  Domingos(Año1= Año_base,Año2= Año_Final)-Domingos(Año1= Año_base,Año2= Año_inicial-1)
print(Cuenta)