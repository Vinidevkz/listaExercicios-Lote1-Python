n = int(input("Digite um número inteiro: "))

i = 2

#Calcula o fatorial
def calculaFatorial(valor):
    results = 0

    if results == 0:
        results = valor * i
    else:
        results = results * i   
    return results
#

while i <= n:
    total = 1 + (1/calculaFatorial(i))
    print("1 + 1 /", i, " = ", total)
    i = i + 1
