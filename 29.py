tipoInvestimento = int(input("Digite o tipo de investimento (1 = Poupança ou 2 = Renda Fixa): "))
valorInvestido = int(input("Digite o valor investido: "))

if tipoInvestimento == 1:
    rendimento = ((valorInvestido * 3)//100)
    total =  rendimento + valorInvestido
    print("O seu dinheiro rendeu: ", rendimento, ". Total: ", total)
elif tipoInvestimento == 2:
    rendimento = ((valorInvestido * 5)//100)
    total =  rendimento + valorInvestido
    print("O seu dinheiro rendeu:", rendimento, "em um mês. Total:", total)
else:
    print("Investimento inválido.")
