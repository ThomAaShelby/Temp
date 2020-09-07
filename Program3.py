a = int(input("Entr Integer"))

ini = 1

for x in range(1, a):
    if x == 1:
        print(ini, " ", end='')

    elif x/2 != 0:
        ini = ini + 2
        print(ini, " ", end='')

    elif x/2 == 0:
        print(ini, " ", end='')