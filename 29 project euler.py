numero = 0
Posicion1 = 0
Lista = []
print(numero)
for b in range(2,101):
    for a in range (2,101) : 
        numero = b ** a
        Lista.append(numero)
for a in Lista :
    Posicion2 = 0
    for c in Lista : 
        if a == c :           
            if Posicion1 != Posicion2 :
                del Lista[Posicion2]
        Posicion2 += 1
    Posicion1 += 1 

print(len(Lista))