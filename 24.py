n1 = 3

d2 = n1 % 2
d3 = n1 % 3

if(d2 == 0):
    if(d3 == 0):
        print("O número é divisível por 2 e por 3.")
    else:
        print("O número é divisível apenas por 2.")
elif(d3 == 0):
    print("O número é divisível apenas por 3.")
else:
    print("O número não é divisível por 2 nem por 3.")