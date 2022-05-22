def occurence(lettrec, chaine):
    n = 0
    for i in range(len(chaine)):
        if chaine[i] == lettrec:
            n += 1
    print(n)