Numero = 0
Fibonachi = [1,1]
Suma = 0
Brake = 0
while Brake <1000 :
    Suma = Fibonachi[Numero]+Fibonachi[Numero+1]  
    Numero += 1 
    Fibonachi.append(Suma)
    Brake = len(str(Suma))
## el numero 2 son los dos numeros iniciales del fibonachi por lo tanto lo sumamos al final.
print(Numero+2)