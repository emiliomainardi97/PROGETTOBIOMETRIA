import Inizializza
from itertools import combinations

'''
    CONTEGGIO DEL NUMERO DI PERSONE PRESENTI NELL'IMMAGINE
'''

def countPerson(all_peaks):
    max = 0

    for i in range(len(all_peaks)):
        if max < len(all_peaks[i]):
            max = len(all_peaks[i])

    valori = []

    for i in range(len(all_peaks)):
        valori.append(len(all_peaks[i]))

    valoriCount = []

    for i in range(max+1):
        valoriCount.append(valori.count(i))

    max1 = 0

    for i in range(len(valoriCount)):
        if max1 < valoriCount[i]:
            max1 = i

    return max1

'''
    CALCOLO DELLE COORDINATE DELLE PARTI DEL CORPO PER CIASCUN COPPIA DI PERSONE PRESENTI NELL'IMMAGINE
'''

def calcoloFinale(all_peaks):
    max = countPerson(all_peaks)

    lista = []
    valoriDaOrdinare = []

    for j in range(max):
        valoriDaOrdinare.append(j)
        listTemp = []
        for i in range(len(all_peaks)):
            if j < len(all_peaks[i]):
                listTemp.append(all_peaks[i][j])
            else:
                listTemp.append((0, 0))
        lista.append(listTemp)

    listaCoppie = []

    comb = combinations(valoriDaOrdinare, 2)

    lis = list(comb)

    for j in range(len(lis)):
        x = lis[j][0]
        y = lis[j][1]

        dict = Inizializza.inizializzazione()

        player1 = lista[x]
        player2 = lista[y]

        for i in range(len(player1)):
            a1 = player1[i][0]
            b1 = player1[i][1]
            Inizializza.assegnaValoriPlayer1(dict,i,a1,b1)
            a2 = player2[i][0]
            b2 = player2[i][1]
            Inizializza.assegnaValoriPlayer2(dict,i,a2,b2)

        listaCoppie.append(dict)

    return listaCoppie, lis

