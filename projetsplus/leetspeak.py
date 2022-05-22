dico = {"a": "4", "b": "8", "c": "(", "d": ")", "e": "3", "f": "|=", "g": "6", "h": "#", "i": "|", "j": "]", "k": "|<", "l": "1", "m": "^^", "n": "^", "o": "0", "p": "|>", "q": "9", "r": "|`", "s": "5", "t": "7", "u": "µ", "v": "|/", "w": "VV", "x": "><", "y": "`/", "z": "2"}
mot = "oui"
nouveaumot = ""
for i in range(len(mot)):
    nouveaumot = dico.get(i)
    print(nouveaumot)