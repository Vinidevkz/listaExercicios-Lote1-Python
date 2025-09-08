n1 = 3
i = n1 - 1

results = 0

while i != 0:
    if results == 0:
        results = n1 * i
    else:
        results = results * i 
    total = 1 + (1/results)
    print("1 + 1/",results, "=", total)
    i = i - 1
print("O fatorial de", n1, "é", results)
