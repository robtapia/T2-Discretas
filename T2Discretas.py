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
        print(i)
    return d[largo]




#n=4
#print(encontrarPalabras(["a","jaj","sk"],n))

def conteo(n):
    lista=[None]*(n+1)
    lista[0]=1
    lista[1]=1
    lista[2]=2
    for x in range(3,n+1):
        lista[x]=lista[x-1]+lista[x-2]+lista[x-3]
    return lista[n]

n=1000
print(float(4^n)/conteo(n))
