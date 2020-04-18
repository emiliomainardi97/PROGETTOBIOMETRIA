import cv2,os

vidcap = cv2.VideoCapture('videos/prova.mp4')
os.chdir('C:\Frame_Estratti')
success,image = vidcap.read()
count = 0
success = True
while success:
     cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
     success,image = vidcap.read()
     print ('Read a new frame: ', success)
     count += 1