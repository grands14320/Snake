schowek = []
licznik = 0
with open(r"D:\zadanie.txt", "r+") as f:
    odczyt = f.readlines()
    print()
    for zdanie in odczyt:
        licznik = 0
        for litera in range(0, len(zdanie)):
            if len(zdanie) == litera + licznik:
                break
            if zdanie[litera + licznik] == "<":
                schowek.append(zdanie[litera + licznik])
                j = litera + licznik
                while zdanie[j] != '>':
                    j = j + 1
                    schowek.append(zdanie[j].upper())
                    licznik = licznik + 1
            else:
                litera = litera + licznik
                schowek.append(zdanie[litera])
    print(schowek)
    print("".join(schowek),end='')

    xd
    tylko c++
