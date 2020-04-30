'''
INIZIALIZZAZIONE FEATURES COMPLETE

'''

def inizializzazione():
    dict = {'nose1': (0, 0), 'nose2': (0, 0), 'neck1': (0, 0), 'neck2': (0, 0), 'right_shoulder1': (0, 0),
            'right_shoulder2': (0, 0), 'right_elbow1': (0, 0), 'right_elbow2': (0, 0), 'right_wrist1': (0, 0),
            'right_wrist2': (0, 0), 'left_shoulder1': (0, 0),
            'left_shoulder2': (0, 0), 'left_elbow1': (0, 0), 'left_elbow2': (0, 0), 'left_wrist1': (0, 0),
            'left_wrist2': (0, 0), 'right_hip1': (0, 0), 'right_hip2': (0, 0), 'right_knee1': (0, 0),
            'right_knee2': (0, 0),
            'right_ankle1': (0, 0), 'right_ankle2': (0, 0), 'left_hip1': (0, 0), 'left_hip2': (0, 0),
            'left_knee1': (0, 0),
            'left_knee2': (0, 0), 'left_ankle1': (0, 0), 'left_ankle2': (0, 0), 'right_eye1': (0, 0),
            'right_eye2': (0, 0),
            'left_eye1': (0, 0), 'left_eye2': (0, 0), 'right_ear1': (0, 0), 'right_ear2': (0, 0), 'left_ear1': (0, 0),
            'left_ear2': (0, 0), 'background1': (0, 0), 'background2': (0, 0)}

    return dict

'''

ASSEGNAMENTO VALORI AL DICT

'''

def assegnaValori(dict,i,j,a,b):
    if (i == 0 and j == 0):
        dict['nose1'] = (a, b)
    if (i == 0 and j == 1):
        dict['nose2'] = (a, b)
    if (i == 1 and j == 0):
        dict['neck1'] = (a, b)
    if (i == 1 and j == 1):
        dict['neck2'] = (a, b)
    if (i == 2 and j == 0):
        dict['right_shoulder1'] = (a, b)
    if (i == 2 and j == 1):
        dict['right_shoulder2'] = (a, b)
    if (i == 3 and j == 0):
        dict['right_elbow1'] = (a, b)
    if (i == 3 and j == 1):
        dict['right_elbow2'] = (a, b)
    if (i == 4 and j == 0):
        dict['right_wrist1'] = (a, b)
    if (i == 4 and j == 1):
        dict['right_wrist2'] = (a, b)
    if (i == 5 and j == 0):
        dict['left_shoulder1'] = (a, b)
    if (i == 5 and j == 1):
        dict['left_shoulder2'] = (a, b)
    if (i == 6 and j == 0):
        dict['left_elbow1'] = (a, b)
    if (i == 6 and j == 1):
        dict['left_elbow2'] = (a, b)
    if (i == 7 and j == 0):
        dict['left_wrist1'] = (a, b)
    if (i == 7 and j == 1):
        dict['left_wrist2'] = (a, b)
    if (i == 8 and j == 0):
        dict['right_hip1'] = (a, b)
    if (i == 8 and j == 1):
        dict['right_hip2'] = (a, b)
    if (i == 9 and j == 0):
        dict['right_knee1'] = (a, b)
    if (i == 9 and j == 1):
        dict['right_knee2'] = (a, b)
    if (i == 10 and j == 0):
        dict['right_ankle1'] = (a, b)
    if (i == 10 and j == 1):
        dict['right_ankle2'] = (a, b)
    if (i == 11 and j == 0):
        dict['left_hip1'] = (a, b)
    if (i == 11 and j == 1):
        dict['left_hip2'] = (a, b)
    if (i == 12 and j == 0):
        dict['left_knee1'] = (a, b)
    if (i == 12 and j == 1):
        dict['left_knee2'] = (a, b)
    if (i == 13 and j == 0):
        dict['left_ankle1'] = (a, b)
    if (i == 13 and j == 1):
        dict['left_ankle2'] = (a, b)
    if (i == 14 and j == 0):
        dict['right_eye1'] = (a, b)
    if (i == 14 and j == 1):
        dict['right_eye2'] = (a, b)
    if (i == 15 and j == 0):
        dict['left_eye1'] = (a, b)
    if (i == 15 and j == 1):
        dict['left_eye2'] = (a, b)
    if (i == 16 and j == 0):
        dict['right_ear1'] = (a, b)
    if (i == 16 and j == 1):
        dict['right_ear2'] = (a, b)
    if (i == 17 and j == 0):
        dict['left_ear1'] = (a, b)
    if (i == 17 and j == 1):
        dict['left_ear2'] = (a, b)
    if (i == 18 and j == 0):
        dict['background1'] = (a, b)
    if (i == 18 and j == 1):
        dict['background2'] = (a, b)