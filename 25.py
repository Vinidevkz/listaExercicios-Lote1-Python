hi = 15
mi = 30
hf = 15
mf = 29

if((hi > 23 or hf > 23) and (mi > 59 or mf > 59)):
    print("Números inválidos.")
elif(hi == hf and mi == mf):
    print("O jogo durou 24 horas exatas.")
else:
    th = hi #15 horas e
    tm = mi #30 minutos
    count = 0
    while not (th == hf and tm == mf):
        if(tm == 59):
            if(th == 23):
                th = 0
                tm = 0
            else:
                th = th + 1
                tm = 0
        else:
            tm = tm + 1
        count = count + 1
        print(count)
    th = count // 60
    tm = count % 60
    print("O jogo durou", th, "horas e", tm, "minutos")