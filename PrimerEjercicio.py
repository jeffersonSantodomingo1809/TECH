S = input("Ingrese un carácter alfanumérico: ")
NImpar = []
NP = []
mayusculas = []
minusculas = []
tam = len(S)
if 0 <= tam <= 1000:
    for n in S:
        if n.isdigit():
            if int(n) % 2 != 0:
                NImpar.append(n)
            else:
               NP.append(n)
        elif n.isupper():
            mayusculas.append(n)
        elif n.islower():
            minusculas.append(n)
    resultado = "".join(sorted(minusculas) + sorted(mayusculas) + sorted(NImpar) + sorted(NP))
    print(resultado)
else:
    print("Ingrese una frase palabra no mayor a 1000")