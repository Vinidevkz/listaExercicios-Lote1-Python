n1 = input(int("Digite o primeiro valor:"))
n2 = input(int("Digite o segundo valor:"))
if n2 >= n1:
    print("O segundo valor deve ser maior que o primeiro.")
else:
    n3 = input(int("Digite o terceiro valor:"))
    if n3 >= n2:
        print("O terceiro valor deve ser maior que o primeiro.")
    else:
        n4 = input(int("Digite o quarto valor:"))

if(n4 < 1):
    print(n4, n1, n2, n3)
elif(n4 < n2):
    print(n1, n4, n2, n3)
elif(n4< n3):
    print(n1, n2, n4, n3)
else:
    print(n1, n2, n3, n4)

