n1 = 8
n2 = 10
n3 = 7
n4 = 7

media = (n1 + n2 + n3 + n4) // 4
print(media)

if media >= 6.0:
    print("APROVADO")
elif media >= 3.0 and media < 6.0:
    print("EXAME")
else:
    print("RETIDO")