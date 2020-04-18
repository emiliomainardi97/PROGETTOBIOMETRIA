import math

def control(x,y):

    if((x[0] == 0 and x[1] == 0) or (y[0] == 0 and y[1] == 0)):
        return 0
    else:
        return calcoloDist(x,y)

def selectPlayer1(dict):
    dist = []

    nose1 = dict['nose1']
    nose2 = dict['nose2']

    dist.append(control(nose1,nose2))

    right_shoulder2 = dict['right_shoulder2']
    left_shoulder2 = dict['left_shoulder2']

    media_1 = (right_shoulder2[0] + left_shoulder2[0])/2
    print(media_1)
    media_2 = (right_shoulder2[1] + left_shoulder2[1])/2
    print(media_2)
    media_shoulder2 = (media_1,media_2)
    dist.append(control(nose1,media_shoulder2))



    return dist

def calcoloDist(x,y):

    x1 = x[0]
    x2 = x[1]
    y1 = y[0]
    y2 = y[1]

    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return dist.__round__(2)


print(calcoloDist((0,5),(0,12)))