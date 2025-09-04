mediaMensal = 500
precoAtual = 30

if mediaMensal < 500 and precoAtual < 30:
    novoPreco = ((precoAtual*10)//100) + precoAtual
    print(novoPreco)
elif mediaMensal >= 500 and (precoAtual >= 30 or precoAtual < 80):
    novoPreco = ((precoAtual*15)//100) + precoAtual
    print(novoPreco)
elif mediaMensal >= 1000 and precoAtual >= 80:
    novoPreco = precoAtual - ((precoAtual*5)//100)
    print(novoPreco)
else:
    novoPreco = precoAtual
