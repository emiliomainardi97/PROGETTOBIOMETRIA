import math


def control(x, y):
    if ((x[0] == 0 and x[1] == 0) or (y[0] == 0 and y[1] == 0)):
        return 0
    else:
        return calcoloDist(x, y)


def selectPlayer1(dict):
    dist = []
    list = []

    '''
    CALCOLO DISTANZE NASO CON:
    -Naso
    -Petto(media)

    '''

    nose1 = dict['nose1']
    nose2 = dict['nose2']

    dist.append(control(nose1, nose2))
    list.append((nose1, nose2))

    right_shoulder2 = dict['right_shoulder2']
    left_shoulder2 = dict['left_shoulder2']

    # MEDIA SPALLA DESTRA - SPALLA SINISTRA (petto)

    media_1 = (right_shoulder2[0] + left_shoulder2[0]) / 2
    media_2 = (right_shoulder2[1] + left_shoulder2[1]) / 2
    media_shoulder2 = (media_1, media_2)
    dist.append(control(nose1, media_shoulder2))

    '''
    CALCOLO DISTANZE GOMITO DESTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra

    '''

    right_elbow1 = dict['right_elbow1']
    dist.append(control(right_elbow1, nose2))
    list.append((right_elbow1, nose2))

    right_hip2 = dict['right_hip2']
    dist.append(control(right_elbow1, right_hip2))
    list.append((right_elbow1, right_hip2))

    left_hip2 = dict['left_hip2']
    dist.append(control(right_elbow1, left_hip2))
    list.append((right_elbow1, left_hip2))

    '''
    CALCOLO DISTANZE GOMITO SINISTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra

    '''

    left_elbow1 = dict['left_elbow1']
    dist.append(control(left_elbow1, nose2))
    list.append((left_elbow1, nose2))

    right_hip2 = dict['right_hip2']
    dist.append(control(left_elbow1, right_hip2))
    list.append((left_elbow1, right_hip2))

    left_hip2 = dict['left_hip2']
    dist.append(control(left_elbow1, left_hip2))
    list.append((left_elbow1, left_hip2))

    '''
    CALCOLO DISTANZE GINOCCHIO DESTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra
    -Ginocchio destro
    -Ginocchio sinistro

    '''

    right_knee1 = dict['right_knee1']
    dist.append(control(right_knee1, nose2))
    list.append((right_knee1, nose2))

    dist.append(control(right_knee1, right_hip2))
    list.append((right_knee1, right_hip2))

    dist.append(control(right_knee1, left_hip2))
    list.append((right_knee1, left_hip2))

    right_knee2 = dict['right_knee2']
    dist.append(control(right_knee1, right_knee2))
    list.append((right_knee1, right_knee2))

    left_knee2 = dict['left_knee2']
    dist.append(control(right_knee1, left_knee2))
    list.append((right_knee1, left_knee2))

    '''
    CALCOLO DISTANZE GINOCCHIO SINISTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra
    -Ginocchio destro
    -Ginocchio sinistro

    '''

    left_knee1 = dict['left_knee1']
    dist.append(control(left_knee1, nose2))
    list.append((left_knee1, nose2))

    dist.append(control(left_knee1, right_hip2))
    list.append((left_knee1, right_hip2))

    dist.append(control(left_knee1, left_hip2))
    list.append((left_knee1, left_hip2))

    dist.append(control(left_knee1, right_knee2))
    list.append((left_knee1, right_knee2))

    dist.append(control(left_knee1, left_knee2))
    list.append((left_knee1, left_knee2))

    '''
    CALCOLO DISTANZE CAVIGLIA DESTRA CON:
    -Caviglia destra
    -Caviglia sinistra
    -Anca sinistra
    -Anca destra
    -Ginocchio destro
    -Ginocchio sinistro

    '''

    right_ankle1 = dict['right_ankle1']
    right_ankle2 = dict['right_ankle2']
    left_ankle2 = dict['left_ankle2']

    dist.append(control(right_ankle1, left_ankle2))
    list.append((right_ankle1, left_ankle2))

    dist.append(control(right_ankle1, right_ankle2))
    list.append((right_ankle1, right_ankle2))

    dist.append(control(right_ankle1, right_hip2))
    list.append((right_ankle1, right_hip2))

    dist.append(control(right_ankle1, left_hip2))
    list.append((right_ankle1, left_hip2))

    dist.append(control(right_ankle1, right_knee2))
    list.append((right_ankle1, right_knee2))

    dist.append(control(right_ankle1, left_knee2))
    list.append((right_ankle1, left_knee2))

    '''
    CALCOLO DISTANZE CAVIGLIA SINISTRA CON:
    -Caviglia destra
    -Caviglia sinistra
    -Anca sinistra
    -Anca destra
    -Ginocchio destro
    -Ginocchio sinistro

    '''
    left_ankle1 = dict['left_ankle1']

    dist.append(control(left_ankle1, left_ankle2))
    list.append((left_ankle1, left_ankle2))

    dist.append(control(left_ankle1, right_ankle2))
    list.append((left_ankle1, right_ankle2))

    dist.append(control(left_ankle1, right_hip2))
    list.append((left_ankle1, right_hip2))

    dist.append(control(left_ankle1, left_hip2))
    list.append((left_ankle1, left_hip2))

    dist.append(control(left_ankle1, right_knee2))
    list.append((left_ankle1, right_knee2))

    dist.append(control(left_ankle1, left_knee2))
    list.append((left_ankle1, left_knee2))

    '''
    CALCOLO DISTANZE POLSO DESTRO CON:
    -Naso
    -Collo
    -Spalla destra
    -Spalla sinistra
    -Petto (media)
    -Polso destro
    -Polso sinistro
    -Gomito destro
    -Gomito sinistro
    -Anca destra
    -Anca sinistra

    '''

    right_wrist1 = dict['right_wrist1']

    dist.append(control(right_wrist1, nose2))
    list.append((right_wrist1, nose2))

    neck2 = dict['neck2']

    dist.append(control(right_wrist1, neck2))
    list.append((right_wrist1, neck2))

    dist.append(control(right_wrist1, right_shoulder2))
    list.append((right_wrist1, right_shoulder2))

    dist.append(control(right_wrist1, left_shoulder2))
    list.append((right_wrist1, left_shoulder2))

    dist.append(control(right_wrist1, media_shoulder2))

    right_wrist2 = dict['right_wrist2']
    left_wrist2 = dict['left_wrist2']

    dist.append(control(right_wrist1, right_wrist2))
    list.append((right_wrist1, right_wrist2))

    dist.append(control(right_wrist1, left_wrist2))
    list.append((right_wrist1, left_wrist2))

    right_elbow2 = dict['right_elbow2']
    left_elbow2 = dict['left_elbow2']

    dist.append(control(right_wrist1, right_elbow2))
    list.append((right_wrist1, right_elbow2))

    dist.append(control(right_wrist1, left_elbow2))
    list.append((right_wrist1, left_elbow2))

    dist.append(control(right_wrist1, right_hip2))
    list.append((right_wrist1, right_hip2))

    dist.append(control(right_wrist1, left_hip2))
    list.append((right_wrist1, left_hip2))

    '''
     CALCOLO DISTANZE POLSO SINISTRO CON:
     -Naso
     -Collo
     -Spalla destra
     -Spalla sinistra
     -Petto (media)
     -Polso destro
     -Polso sinistro
     -Gomito destro
     -Gomito sinistro
     -Anca destra
     -Anca sinistra

     '''

    left_wrist1 = dict['left_wrist1']

    dist.append(control(left_wrist1, nose2))
    list.append((left_wrist1, nose2))

    dist.append(control(left_wrist1, neck2))
    list.append((left_wrist1, neck2))

    dist.append(control(left_wrist1, right_shoulder2))
    list.append((left_wrist1, right_shoulder2))

    dist.append(control(left_wrist1, left_shoulder2))
    list.append((left_wrist1, left_shoulder2))

    dist.append(control(left_wrist1, media_shoulder2))

    dist.append(control(left_wrist1, right_wrist2))
    list.append((left_wrist1, right_wrist2))

    dist.append(control(left_wrist1, left_wrist2))
    list.append((left_wrist1, left_wrist2))

    dist.append(control(left_wrist1, right_elbow2))
    list.append((left_wrist1, right_elbow2))

    dist.append(control(left_wrist1, left_elbow2))
    list.append((left_wrist1, left_elbow2))

    dist.append(control(left_wrist1, right_hip2))
    list.append((left_wrist1, right_hip2))

    dist.append(control(left_wrist1, left_hip2))
    list.append((left_wrist1, left_hip2))

    return dist, list


def selectPlayer2(dict):
    dist = []
    list = []

    '''
    CALCOLO DISTANZE NASO CON:
    -Naso
    -Petto(media)

    '''

    nose2 = dict['nose2']
    nose1 = dict['nose1']

    # dist.append(control(nose2, nose1))
    list.append((nose2, nose1))

    right_shoulder1 = dict['right_shoulder1']
    left_shoulder1 = dict['left_shoulder1']

    # MEDIA SPALLA DESTRA - SPALLA SINISTRA (petto)

    media_1 = (right_shoulder1[0] + left_shoulder1[0]) / 2
    media_2 = (right_shoulder1[1] + left_shoulder1[1]) / 2
    media_shoulder1 = (media_1, media_2)
    dist.append(control(nose2, media_shoulder1))

    '''
    CALCOLO DISTANZE GOMITO DESTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra

    '''

    right_elbow2 = dict['right_elbow2']
    dist.append(control(right_elbow2, nose1))
    list.append((right_elbow2, nose1))

    right_hip1 = dict['right_hip1']
    dist.append(control(right_elbow2, right_hip1))
    list.append((right_elbow2, right_hip1))

    left_hip1 = dict['left_hip1']
    dist.append(control(right_elbow2, left_hip1))
    list.append((right_elbow2, left_hip1))

    '''
    CALCOLO DISTANZE GOMITO SINISTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra

    '''

    left_elbow2 = dict['left_elbow2']
    dist.append(control(left_elbow2, nose1))
    list.append((left_elbow2, nose1))

    right_hip1 = dict['right_hip1']
    dist.append(control(left_elbow2, right_hip1))
    list.append((left_elbow2, right_hip1))

    left_hip1 = dict['left_hip1']
    dist.append(control(left_elbow2, left_hip1))
    list.append((left_elbow2, left_hip1))

    '''
    CALCOLO DISTANZE GINOCCHIO DESTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra
    -Ginocchio destro
    -Ginocchio sinistro

    '''

    right_knee2 = dict['right_knee2']
    dist.append(control(right_knee2, nose1))
    list.append((right_knee2, nose1))

    dist.append(control(right_knee2, right_hip1))
    list.append((right_knee2, right_hip1))

    dist.append(control(right_knee2, left_hip1))
    list.append((right_knee2, left_hip1))

    right_knee1 = dict['right_knee1']
    # dist.append(control(right_knee2, right_knee1))
    list.append((right_knee2, right_knee1))

    left_knee1 = dict['left_knee1']
    dist.append(control(right_knee2, left_knee1))
    list.append((right_knee2, left_knee1))

    '''
    CALCOLO DISTANZE GINOCCHIO SINISTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra
    -Ginocchio destro
    -Ginocchio sinistro

    '''

    left_knee2 = dict['left_knee2']
    dist.append(control(left_knee2, nose1))
    list.append((left_knee2, nose1))

    dist.append(control(left_knee2, right_hip1))
    list.append((left_knee2, right_hip1))

    dist.append(control(left_knee2, left_hip1))
    list.append((left_knee2, left_hip1))

    dist.append(control(left_knee2, right_knee1))
    list.append((left_knee2, right_knee1))

    # dist.append(control(left_knee2, left_knee1))
    list.append((left_knee2, left_knee1))

    '''
    CALCOLO DISTANZE CAVIGLIA DESTRA CON:
    -Caviglia destra
    -Caviglia sinistra
    -Anca sinistra
    -Anca destra
    -Ginocchio destro
    -Ginocchio sinistro

    '''

    right_ankle2 = dict['right_ankle2']
    right_ankle1 = dict['right_ankle1']
    left_ankle1 = dict['left_ankle1']

    # dist.append(control(right_ankle2, left_ankle1))
    list.append((right_ankle2, left_ankle1))

    # dist.append(control(right_ankle2, right_ankle1))
    list.append((right_ankle2, right_ankle1))

    dist.append(control(right_ankle2, right_hip1))
    list.append((right_ankle2, right_hip1))

    dist.append(control(right_ankle2, left_hip1))
    list.append((right_ankle2, left_hip1))

    dist.append(control(right_ankle2, right_knee1))
    list.append((right_ankle2, right_knee1))

    dist.append(control(right_ankle2, left_knee1))
    list.append((right_ankle2, left_knee1))

    '''
    CALCOLO DISTANZE CAVIGLIA SINISTRA CON:
    -Caviglia destra
    -Caviglia sinistra
    -Anca sinistra
    -Anca destra
    -Ginocchio destro
    -Ginocchio sinistro

    '''
    left_ankle2 = dict['left_ankle2']

    # dist.append(control(left_ankle2, left_ankle1))
    list.append((left_ankle2, left_ankle1))

    # dist.append(control(left_ankle2, right_ankle1))
    list.append((left_ankle2, right_ankle1))

    dist.append(control(left_ankle2, right_hip1))
    list.append((left_ankle2, right_hip1))

    dist.append(control(left_ankle2, left_hip1))
    list.append((left_ankle2, left_hip1))

    dist.append(control(left_ankle2, right_knee1))
    list.append((left_ankle2, right_knee1))

    dist.append(control(left_ankle2, left_knee1))
    list.append((left_ankle2, left_knee1))

    '''
    CALCOLO DISTANZE POLSO DESTRO CON:
    -Naso
    -Collo
    -Spalla destra
    -Spalla sinistra
    -Petto (media)
    -Polso destro
    -Polso sinistro
    -Gomito destro
    -Gomito sinistro
    -Anca destra
    -Anca sinistra

    '''

    right_wrist2 = dict['right_wrist2']

    dist.append(control(right_wrist2, nose1))
    list.append((right_wrist2, nose1))

    neck1 = dict['neck1']

    dist.append(control(right_wrist2, neck1))
    list.append((right_wrist2, neck1))

    dist.append(control(right_wrist2, right_shoulder1))
    list.append((right_wrist2, right_shoulder1))

    dist.append(control(right_wrist2, left_shoulder1))
    list.append((right_wrist2, left_shoulder1))

    dist.append(control(right_wrist2, media_shoulder1))

    right_wrist1 = dict['right_wrist1']
    left_wrist1 = dict['left_wrist1']

    # dist.append(control(right_wrist2, right_wrist1))
    list.append((right_wrist2, right_wrist1))

    dist.append(control(right_wrist2, left_wrist1))
    list.append((right_wrist2, left_wrist1))

    right_elbow1 = dict['right_elbow1']
    left_elbow1 = dict['left_elbow1']

    dist.append(control(right_wrist2, right_elbow1))
    list.append((right_wrist2, right_elbow1))

    dist.append(control(right_wrist2, left_elbow1))
    list.append((right_wrist2, left_elbow1))

    dist.append(control(right_wrist2, right_hip1))
    list.append((right_wrist2, right_hip1))

    dist.append(control(right_wrist2, left_hip1))
    list.append((right_wrist2, left_hip1))

    '''
     CALCOLO DISTANZE POLSO SINISTRO CON:
     -Naso
     -Collo
     -Spalla destra
     -Spalla sinistra
     -Petto (media)
     -Polso destro
     -Polso sinistro
     -Gomito destro
     -Gomito sinistro
     -Anca destra
     -Anca sinistra

     '''

    left_wrist2 = dict['left_wrist2']

    dist.append(control(left_wrist2, nose1))
    list.append((left_wrist2, nose1))

    dist.append(control(left_wrist2, neck1))
    list.append((left_wrist2, neck1))

    dist.append(control(left_wrist2, right_shoulder1))
    list.append((left_wrist2, right_shoulder1))

    dist.append(control(left_wrist2, left_shoulder1))
    list.append((left_wrist2, left_shoulder1))

    dist.append(control(left_wrist2, media_shoulder1))

    dist.append(control(left_wrist2, right_wrist1))
    list.append((left_wrist2, right_wrist1))

    # dist.append(control(left_wrist2, left_wrist1))
    list.append((left_wrist2, left_wrist1))

    dist.append(control(left_wrist2, right_elbow1))
    list.append((left_wrist2, right_elbow1))

    dist.append(control(left_wrist2, left_elbow1))
    list.append((left_wrist2, left_elbow1))

    dist.append(control(left_wrist2, right_hip1))
    list.append((left_wrist2, right_hip1))

    dist.append(control(left_wrist2, left_hip1))
    list.append((left_wrist2, left_hip1))

    return dist, list


def calcoloDist(x, y):
    x1 = x[0]
    x2 = x[1]
    y1 = y[0]
    y2 = y[1]

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return dist.__round__(2)
