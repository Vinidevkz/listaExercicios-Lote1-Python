n1 = 1
n2 = 6

if n1 > n2:
    maiorNumero = n1
    menorNumero = n2
else:
    maiorNumero = n2
    menorNumero = n1

sobras = (maiorNumero - menorNumero) - 1
if sobras == 0:
    print("Não há valores entre os números.")
else:
    somaTotal = 0
    count = 1
    while count <= sobras:
        isImpar = (menorNumero + count) % 2
        if isImpar != 0:
            somaTotal = somaTotal + (menorNumero + count)
        count = count + 1
    print("Soma dos ímpares:",somaTotal)