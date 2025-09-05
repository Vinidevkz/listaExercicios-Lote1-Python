dataAtual = 4
mesAtual = 9
anoAtual = 2025

dataNasc = 1
mesNasc = 11
anoNasc = 2005

diasTotais = 0
anosTotais = (anoAtual - anoNasc) - 1

while anoNasc <= anoAtual:
    bissextoVerificancao = anoNasc % 400
    if bissextoVerificancao != 0:
        diasTotais = diasTotais + 365
    elif bissextoVerificancao == 0:
        diasTotais = diasTotais + 366
    anoNasc = anoNasc + 1
mesesTotais = (diasTotais // 30) - (12 - mesAtual)

print("Você está vivo a", diasTotais, "dias,", mesesTotais, "meses e", anosTotais, "anos")




