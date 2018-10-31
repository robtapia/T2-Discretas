def encontrarPalabras(alfabeto, largo):
    d = dict()
    d[0] = [""]
    for i in range(1,largo+1):
        words = []
        for w in alfabeto:
            if(i-len(w) >= 0):
                words.extend([x+w for x in d[i-len(w)]])
        words.sort()
        for j in range(len(words)-1):
            if words[j] == words[j+1]:
                print (words[j])
        d[i] = words
        #print(i)
    return d[largo]

n=25
print(float((n^4))/len(encontrarPalabras(["a","jaj","sk"],n)))


