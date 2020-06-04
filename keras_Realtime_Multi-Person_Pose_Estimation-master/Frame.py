'''

ESTRAZIONE DEI FRAME DAI VIDEO

'''

import cv2,os

#path = 'C:\FightDataset\prova'
path ="C:\FightDataset\\fi"

estensione= '_xvid.avi'

os.chdir('C:\HockeyFrame')
count = 0

start = 0 #DA CAMBIARE START E END
end = 1

for i in range(start,end):

    vidcap = cv2.VideoCapture(path + str(i) + estensione)
    success,image = vidcap.read()

    while success:

        image = cv2.resize(image, (1080,1080), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        count += 1