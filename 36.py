iSerie = 1
iFatorial = 0

while iSerie <= 10:
    iFatorial = iSerie - 1
    totalFatorial = 0
    while iFatorial != 0:
        totalFatorial = totalFatorial + (iSerie * iFatorial)
        iFatorial = iFatorial - 1
    iSerie = iSerie + 1
print(totalFatorial)
