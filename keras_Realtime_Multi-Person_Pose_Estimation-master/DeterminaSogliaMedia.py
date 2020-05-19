import pandas

'''
    CALCOLO DELLA SOGLIA DA UTILIZZARE PER SELEZIONARE COPPIE DI PERSONE
    DA CONFRONTARE
'''

def determinaSogliaMedia(path):
    dataframe = pandas.read_csv(path)

    dataset = dataframe.values

    sum = 0
    count = 0

    for i in range(len(dataset)):
        if dataset[i][93] == "fight":
            for j in range(len(dataset[i])-1):
                if dataset[i][j] != 0:
                    sum = sum + dataset[i][j]
                    count = count + 1

    return sum/count

'''
    CONTROLLO PER DETERMINARE SE LA COPPIA DI PERSONE PRESE IN ESAME DEVONO ESSERE O MENO SELEZIONATE PER 
    LA CLASSIFICAZIONE
'''

def control(dist, soglia):
    count = 0

    for i in range(len(dist)):
        if dist[i] <= soglia:
            count = count + 1

    return count / len(dist)