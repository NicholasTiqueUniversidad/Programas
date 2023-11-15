Pen = int
Numerospen = []
NumerosDif = []
Diferencia1 = 0
Diferencia2 = 0
lista1 = []
lista2 = []
def es_pentagonal(num):
    k = (1 + (24 * num + 1) ** 0.5) / 6
    return k.is_integer()
for a in range (1,1000000) :
    Pen = int((a*((a*3)-1))/2)
    Numerospen.append(Pen)
for b in range (0,len(Numerospen)) :
    for c in range (0,len(Numerospen))  :
        Diferencia1 = Numerospen[b]+Numerospen[c]
        Diferencia2 = abs(Numerospen[b]-Numerospen[c])
        if es_pentagonal(Diferencia1) and es_pentagonal(Diferencia2):
            lista2.append(Diferencia1)
            print(Diferencia1)
print(lista2)