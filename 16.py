horasTrabalhadas = 8
valorPHora = 60
descontoPercentual = 8
nDependentes = 2

bruto = horasTrabalhadas * valorPHora
liquido = (bruto - (bruto * (descontoPercentual//100)))
total = liquido + (nDependentes * 100)
print(total)