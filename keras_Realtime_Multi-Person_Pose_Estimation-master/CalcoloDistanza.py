import math

def control(x,y):

    if((x[0] == 0 and x[1] == 0) or (y[0] == 0 and y[1] == 0)):
        return 0
    else:
        return calcoloDist(x,y)

def selectPlayer1(dict):
    dist = []

    '''
    CALCOLO DISTANZE NASO CON:
    -Naso
    -Petto(media)

    '''

    nose1 = dict['nose1']
    nose2 = dict['nose2']

    #dn1n2
    dist.append(control(nose1,nose2))

    right_shoulder2 = dict['right_shoulder2']
    left_shoulder2 = dict['left_shoulder2']

    #MEDIA SPALLA DESTRA - SPALLA SINISTRA (petto)

    media_1 = (right_shoulder2[0] + left_shoulder2[0])/2
    media_2 = (right_shoulder2[1] + left_shoulder2[1])/2
    media_shoulder2 = (media_1,media_2)
    #dn1p2
    dist.append(control(nose1,media_shoulder2))

    '''
    CALCOLO DISTANZE GOMITO DESTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra
    
    '''

    right_elbow1 = dict['right_elbow1']
    #dre1n2
    dist.append(control(right_elbow1,nose2))

    right_hip2 = dict['right_hip2']
    #dre1rh2
    dist.append(control(right_elbow1,right_hip2))

    left_hip2 = dict['left_hip2']
    #dre1lh2
    dist.append(control(right_elbow1, left_hip2))

    '''
    CALCOLO DISTANZE GOMITO SINISTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra

    '''

    left_elbow1 = dict['left_elbow1']
    #dle1n2
    dist.append(control(left_elbow1, nose2))

    right_hip2 = dict['right_hip2']
    #dle1rh2
    dist.append(control(left_elbow1, right_hip2))

    left_hip2 = dict['left_hip2']
    #dle1lh2
    dist.append(control(left_elbow1, left_hip2))


    '''
    CALCOLO DISTANZE GINOCCHIO DESTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra
    -Ginocchio destro
    -Ginocchio sinistro
    
    '''

    right_knee1 = dict['right_knee1']
    #drk1n2
    dist.append(control(right_knee1, nose2))

    #drk1rh2
    dist.append(control(right_knee1, right_hip2))

    #drk1lh2
    dist.append(control(right_knee1, left_hip2))

    right_knee2 = dict['right_knee2']
    #drk1rk2
    dist.append(control(right_knee1, right_knee2))

    left_knee2 = dict['left_knee2']
    #drk1lk2
    dist.append(control(right_knee1,left_knee2))

    '''
    CALCOLO DISTANZE GINOCCHIO SINISTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra
    -Ginocchio destro
    -Ginocchio sinistro

    '''

    left_knee1 = dict['left_knee1']
    #dlk1n2
    dist.append(control(left_knee1, nose2))

    #dlk1rh2
    dist.append(control(left_knee1, right_hip2))

    #dlk1lh2
    dist.append(control(left_knee1, left_hip2))

    #dlk1rk2
    dist.append(control(left_knee1, right_knee2))

    #dlk1lk2
    dist.append(control(left_knee1, left_knee2))

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

    #dra1la2
    dist.append(control(right_ankle1,left_ankle2))

    #dra1ra2
    dist.append(control(right_ankle1,right_ankle2))

    #dra1rh2
    dist.append(control(right_ankle1,right_hip2))

    #dra1lh2
    dist.append(control(right_ankle1, left_hip2))

    #dra1rk2
    dist.append(control(right_ankle1, right_knee2))

    #dra1lk2
    dist.append(control(right_ankle1, left_knee2))

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

    #dla1la2
    dist.append(control(left_ankle1, left_ankle2))

    #dla1ra2
    dist.append(control(left_ankle1, right_ankle2))

    #dla1rh2
    dist.append(control(left_ankle1, right_hip2))

    #dla1lh2
    dist.append(control(left_ankle1, left_hip2))

    #dla1rk2
    dist.append(control(left_ankle1, right_knee2))

    #dla1lk2
    dist.append(control(left_ankle1, left_knee2))


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

    #drw1n2
    dist.append(control(right_wrist1,nose2))

    neck2 = dict['neck2']

    #drw1ne2
    dist.append(control(right_wrist1,neck2))

    #drw1rs2
    dist.append(control(right_wrist1, right_shoulder2))

    #drw1ls2
    dist.append(control(right_wrist1, left_shoulder2))

    #drw1p2
    dist.append(control(right_wrist1, media_shoulder2))

    right_wrist2 = dict['right_wrist2']
    left_wrist2 = dict['left_wrist2']

    #drw1rw2
    dist.append(control(right_wrist1, right_wrist2))

    #drw1lw2
    dist.append(control(right_wrist1, left_wrist2))

    right_elbow2 = dict['right_elbow2']
    left_elbow2 = dict['left_elbow2']

    #drw1re2
    dist.append(control(right_wrist1, right_elbow2))

    #drw1le2
    dist.append(control(right_wrist1, left_elbow2))

    #drw1rh2
    dist.append(control(right_wrist1, right_hip2))

    #drw1lh2
    dist.append(control(right_wrist1, left_hip2))


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

    #dlw1n2
    dist.append(control(left_wrist1, nose2))

    #dlw1ne2
    dist.append(control(left_wrist1, neck2))

    #dlw1rs2
    dist.append(control(left_wrist1, right_shoulder2))

    #dlw1ls2
    dist.append(control(left_wrist1, left_shoulder2))

    #dlw1p2
    dist.append(control(left_wrist1, media_shoulder2))

    #dlw1rw2
    dist.append(control(left_wrist1, right_wrist2))

    #dlw1lw2
    dist.append(control(left_wrist1, left_wrist2))

    #dlw1re2
    dist.append(control(left_wrist1, right_elbow2))

    #dlw1le2
    dist.append(control(left_wrist1, left_elbow2))

    #dlw1rh2
    dist.append(control(left_wrist1, right_hip2))

    #dlw1lh2
    dist.append(control(left_wrist1, left_hip2))

    return dist


def selectPlayer2(dict):
    dist = []

    '''
    CALCOLO DISTANZE NASO CON:
    -Naso
    -Petto(media)

    '''

    nose2 = dict['nose2']
    nose1 = dict['nose1']

   # dist.append(control(nose2, nose1))

    right_shoulder1 = dict['right_shoulder1']
    left_shoulder1 = dict['left_shoulder1']

    # MEDIA SPALLA DESTRA - SPALLA SINISTRA (petto)

    media_1 = (right_shoulder1[0] + left_shoulder1[0]) / 2
    media_2 = (right_shoulder1[1] + left_shoulder1[1]) / 2
    media_shoulder1 = (media_1, media_2)

    #dn2p1
    dist.append(control(nose2, media_shoulder1))

    '''
    CALCOLO DISTANZE GOMITO DESTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra

    '''

    right_elbow2 = dict['right_elbow2']
    #dre2n1
    dist.append(control(right_elbow2, nose1))

    right_hip1 = dict['right_hip1']
    #dre2rh1
    dist.append(control(right_elbow2, right_hip1))

    left_hip1 = dict['left_hip1']
    #dre2lh1
    dist.append(control(right_elbow2, left_hip1))

    '''
    CALCOLO DISTANZE GOMITO SINISTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra

    '''

    left_elbow2 = dict['left_elbow2']
    #dle2n1
    dist.append(control(left_elbow2, nose1))

    right_hip1 = dict['right_hip1']
    #dle2rh1
    dist.append(control(left_elbow2, right_hip1))

    left_hip1 = dict['left_hip1']
    #dle2lh1
    dist.append(control(left_elbow2, left_hip1))

    '''
    CALCOLO DISTANZE GINOCCHIO DESTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra
    -Ginocchio destro
    -Ginocchio sinistro

    '''

    right_knee2 = dict['right_knee2']
    #drk2n1
    dist.append(control(right_knee2, nose1))

    #drk2rh1
    dist.append(control(right_knee2, right_hip1))

    #drk2lh1
    dist.append(control(right_knee2, left_hip1))

    right_knee1 = dict['right_knee1']
   # dist.append(control(right_knee2, right_knee1))

    left_knee1 = dict['left_knee1']

    #drk2lk1
    dist.append(control(right_knee2, left_knee1))

    '''
    CALCOLO DISTANZE GINOCCHIO SINISTRO CON:
    -Naso
    -Anca destra
    -Anca sinistra
    -Ginocchio destro
    -Ginocchio sinistro

    '''

    left_knee2 = dict['left_knee2']

    #dlk2n1
    dist.append(control(left_knee2, nose1))

    #dlk2rh1
    dist.append(control(left_knee2, right_hip1))

    #dlk2lh1
    dist.append(control(left_knee2, left_hip1))

    #dlk2rk1
    dist.append(control(left_knee2, right_knee1))

   # dist.append(control(left_knee2, left_knee1))

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

    #dist.append(control(right_ankle2, left_ankle1))

    #dist.append(control(right_ankle2, right_ankle1))

    #dra2rh1
    dist.append(control(right_ankle2, right_hip1))

    #dra2lh1
    dist.append(control(right_ankle2, left_hip1))

    #dra2rk1
    dist.append(control(right_ankle2, right_knee1))

    #dra2lk1
    dist.append(control(right_ankle2, left_knee1))

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

    #dist.append(control(left_ankle2, left_ankle1))

    #dist.append(control(left_ankle2, right_ankle1))

    #dla2rh1
    dist.append(control(left_ankle2, right_hip1))

    #dla2lh1
    dist.append(control(left_ankle2, left_hip1))

    #dla2rk1
    dist.append(control(left_ankle2, right_knee1))

    #dla2lk1
    dist.append(control(left_ankle2, left_knee1))

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

    #drw2n1
    dist.append(control(right_wrist2, nose1))

    neck1 = dict['neck1']

    #drw2ne1
    dist.append(control(right_wrist2, neck1))

    #drw2rs1
    dist.append(control(right_wrist2, right_shoulder1))

    #drw2ls1
    dist.append(control(right_wrist2, left_shoulder1))

    #drw2p1
    dist.append(control(right_wrist2, media_shoulder1))

    right_wrist1 = dict['right_wrist1']
    left_wrist1 = dict['left_wrist1']

   # dist.append(control(right_wrist2, right_wrist1))

   # dist.append(control(right_wrist2, left_wrist1))

    right_elbow1 = dict['right_elbow1']
    left_elbow1 = dict['left_elbow1']

    #drw2re1
    dist.append(control(right_wrist2, right_elbow1))

    #drw2le1
    dist.append(control(right_wrist2, left_elbow1))

    #drw2rh1
    dist.append(control(right_wrist2, right_hip1))

    #drw2lh1
    dist.append(control(right_wrist2, left_hip1))

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

    #dlw2n1
    dist.append(control(left_wrist2, nose1))

    #dlw2ne1
    dist.append(control(left_wrist2, neck1))

    #dlw2rs1
    dist.append(control(left_wrist2, right_shoulder1))

    #dlw2ls1
    dist.append(control(left_wrist2, left_shoulder1))

    #dlw2p1
    dist.append(control(left_wrist2, media_shoulder1))


   # dist.append(control(left_wrist2, right_wrist1))

   # dist.append(control(left_wrist2, left_wrist1))

    #dlw2re1
    dist.append(control(left_wrist2, right_elbow1))

    #dlw2le1
    dist.append(control(left_wrist2, left_elbow1))

    #dlw2rh1
    dist.append(control(left_wrist2, right_hip1))

    #dlw2lh1
    dist.append(control(left_wrist2, left_hip1))

    return dist


def calcoloDist(x,y):

    x1 = x[0]
    x2 = x[1]
    y1 = y[0]
    y2 = y[1]

    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return dist.__round__(2)
