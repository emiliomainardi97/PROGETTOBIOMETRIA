import pandas as pd
import glob
import sys
import matplotlib.pyplot as plt
import csv
import os


def salva_csv(dict,value):
    file_exists = os.path.isfile('dataset.csv')
    with open('dataset.csv', mode='a', newline='') as csv_file:
        fieldnames = ['nose1x', 'neck1x',
                       'right_shoulder1x', 'right_elbow1x', 'right_wrist1x',
                       'left_shoulder1x', 'left_elbow1x', 'left_wrist1x',
                       'right_hip1x', 'right_knee1x', 'right_ankle1x',
                       'left_hip1x', 'left_knee1x', 'left_ankle1x',
                       'right_eye1x', 'left_eye1x', 'right_ear1x', 'left_ear1x', 'background1x',
                       'nose1y', 'neck1y',
                       'right_shoulder1y', 'right_elbow1y', 'right_wrist1y',
                       'left_shoulder1y', 'left_elbow1y', 'left_wrist1y',
                       'right_hip1y', 'right_knee1y', 'right_ankle1y',
                       'left_hip1y', 'left_knee1y', 'left_ankle1y',
                       'right_eye1y', 'left_eye1y', 'right_ear1y', 'left_ear1y', 'background1y',
                       'nose2x', 'neck2x',
                       'right_shoulder2x', 'right_elbow2x', 'right_wrist2x',
                       'left_shoulder2x', 'left_elbow2x', 'left_wrist2x',
                       'right_hip2x', 'right_knee2x', 'right_ankle2x',
                       'left_hip2x', 'left_knee2x', 'left_ankle2x',
                       'right_eye2x', 'left_eye2x', 'right_ear2x', 'left_ear2x', 'background2x',
                       'nose2y', 'neck2y',
                       'right_shoulder2y', 'right_elbow2y', 'right_wrist2y',
                       'left_shoulder2y', 'left_elbow2y', 'left_wrist2y',
                       'right_hip2y', 'right_knee2y', 'right_ankle2y',
                       'left_hip2y', 'left_knee2y', 'left_ankle2y',
                       'right_eye2y', 'left_eye2y', 'right_ear2y', 'left_ear2y', 'background2y','label']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        writer.writerow({
                       'nose1x':dict['nose1'][0],'neck1x':dict['neck1'][0],
                       'right_shoulder1x':dict['right_shoulder1'][0], 'right_elbow1x':dict['right_elbow1'][0], 'right_wrist1x':dict['right_wrist1'][0],
                       'left_shoulder1x':dict['left_shoulder1'][0], 'left_elbow1x':dict['left_elbow1'][0], 'left_wrist1x':dict['left_wrist1'][0],
                       'right_hip1x':dict['right_hip1'][0], 'right_knee1x':dict['right_knee1'][0], 'right_ankle1x':dict['right_ankle1'][0],
                       'left_hip1x':dict['left_hip1'][0], 'left_knee1x':dict['left_knee1'][0], 'left_ankle1x':dict['left_ankle1'][0],
                       'right_eye1x':dict['right_eye1'][0], 'left_eye1x':dict['left_eye1'][0], 'right_ear1x':dict['right_ear1'][0], 'left_ear1x':dict['left_ear1'][0], 'background1x':dict['background1'][0],

                       'nose1y':dict['nose1'][1],'neck1y':dict['neck1'][1],
                       'right_shoulder1y':dict['right_shoulder1'][1], 'right_elbow1y':dict['right_elbow1'][1], 'right_wrist1y':dict['right_wrist1'][1],
                       'left_shoulder1y':dict['left_shoulder1'][1], 'left_elbow1y':dict['left_elbow1'][1], 'left_wrist1y':dict['left_wrist1'][1],
                       'right_hip1y':dict['right_hip1'][1], 'right_knee1y':dict['right_knee1'][1], 'right_ankle1y':dict['right_ankle1'][1],
                       'left_hip1y':dict['left_hip1'][1], 'left_knee1y':dict['left_knee1'][1], 'left_ankle1y':dict['left_ankle1'][1],
                       'right_eye1y':dict['right_eye1'][1], 'left_eye1y':dict['left_eye1'][1], 'right_ear1y':dict['right_ear1'][1], 'left_ear1y':dict['left_ear1'][1], 'background1y':dict['background1'][1],

                       'nose2x':dict['nose2'][0],'neck2x':dict['neck2'][0],'right_shoulder2x':dict['right_shoulder2'][0], 'right_elbow2x':dict['right_elbow2'][0], 'right_wrist2x':dict['right_wrist2'][0],
                       'left_shoulder2x':dict['left_shoulder2'][0], 'left_elbow2x':dict['left_elbow2'][0], 'left_wrist2x':dict['left_wrist2'][0],
                       'right_hip2x':dict['right_hip2'][0], 'right_knee2x':dict['right_knee2'][0], 'right_ankle2x':dict['right_ankle2'][0],
                       'left_hip2x':dict['left_hip2'][0], 'left_knee2x':dict['left_knee2'][0], 'left_ankle2x':dict['left_ankle2'][0],
                       'right_eye2x':dict['right_eye2'][0], 'left_eye2x':dict['left_eye2'][0], 'right_ear2x':dict['right_ear2'][0], 'left_ear2x':dict['left_ear2'][0], 'background2x':dict['background2'][0],

                       'nose2y':dict['nose2'][1], 'neck2y':dict['neck2'][1],
                       'right_shoulder2y':dict['right_shoulder2'][1], 'right_elbow2y':dict['right_elbow2'][1], 'right_wrist2y':dict['right_wrist2'][1],
                       'left_shoulder2y':dict['left_shoulder2'][1], 'left_elbow2y':dict['left_elbow2'][1], 'left_wrist2y':dict['left_wrist2'][1],
                       'right_hip2y':dict['right_hip2'][1], 'right_knee2y':dict['right_knee2'][1], 'right_ankle2y':dict['right_ankle2'][1],
                       'left_hip2y':dict['left_hip2'][1], 'left_knee2y':dict['left_knee2'][1], 'left_ankle2y':dict['left_ankle2'][1],
                       'right_eye2y':dict['right_eye2'][1], 'left_eye2y':dict['left_eye2'][1], 'right_ear2y':dict['right_ear2'][1],
                       'left_ear2y':dict['left_ear2'][1], 'background2y':dict['background2'][1], 'label':value})

def salva_csv_dist(list1,list2, value):
    file_exists = os.path.isfile('dataset_dist.csv')
    with open('dataset_dist.csv', mode='a', newline='') as csv_file:

        fieldnames = [
            'dn1n2','dn1p2',
            'dre1n2','dre1rh2','dre1lh2','dle1n2','dle1rh2','dle1lh2','drk1n2','drk1rh2','drk1lh2',
            'drk1rk2','drk1lk2','dlk1n2','dlk1rh2','dlk1lh2','dlk1rk2','dlk1lk2','dra1la2','dra1ra2','dra1rh2','dra1lh2',
            'dra1rk2','dra1lk2','dla1la2','dla1ra2','dla1rh2','dla1lh2','dla1rk2','dla1lk2','drw1n2','drw1ne2','drw1rs2','drw1ls2',
            'drw1p2','drw1rw2','drw1lw2','drw1re2','drw1le2','drw1rh2','drw1lh2','dlw1n2','dlw1ne2','dlw1rs2','dlw1ls2','dlw1p2',
            'dlw1rw2','dlw1lw2','dlw1re2','dlw1le2','dlw1rh2','dlw1lh2',

            'dn2p1',
            'dre2n1', 'dre2rh1', 'dre2lh1', 'dle2n1', 'dle2rh1', 'dle2lh1', 'drk2n1', 'drk2rh1', 'drk2lh1',
            'drk2lk1', 'dlk2n1', 'dlk2rh1', 'dlk2lh1', 'dlk2rk1', 'dra2rh1',
            'dra2lh1',
            'dra2rk1', 'dra2lk1', 'dla2rh1', 'dla2lh1', 'dla2rk1', 'dla2lk1', 'drw2n1', 'drw2ne1',
            'drw2rs1', 'drw2ls1',
            'drw2p1', 'drw2re1', 'drw2le1', 'drw2rh1', 'drw2lh1', 'dlw2n1', 'dlw2ne1', 'dlw2rs1',
            'dlw2ls1', 'dlw2p1',
            'dlw2re1', 'dlw2le1', 'dlw2rh1', 'dlw2lh1','label'
        ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            fieldnames[0]: list1[0],
            fieldnames[1]: list1[1],
            fieldnames[2]: list1[2],
            fieldnames[3]: list1[3],
            fieldnames[4]: list1[4],
            fieldnames[5]: list1[5],
            fieldnames[6]: list1[6],
            fieldnames[7]: list1[7],
            fieldnames[8]: list1[8],
            fieldnames[9]: list1[9],
            fieldnames[10]: list1[10],
            fieldnames[11]: list1[11],
            fieldnames[12]: list1[12],
            fieldnames[13]: list1[13],
            fieldnames[14]: list1[14],
            fieldnames[15]: list1[15],
            fieldnames[16]: list1[16],
            fieldnames[17]: list1[17],
            fieldnames[18]: list1[18],
            fieldnames[19]: list1[19],
            fieldnames[20]: list1[20],
            fieldnames[21]: list1[21],
            fieldnames[22]: list1[22],
            fieldnames[23]: list1[23],
            fieldnames[24]: list1[24],
            fieldnames[25]: list1[25],
            fieldnames[26]: list1[26],
            fieldnames[27]: list1[27],
            fieldnames[28]: list1[28],
            fieldnames[29]: list1[29],
            fieldnames[30]: list1[30],
            fieldnames[31]: list1[31],
            fieldnames[32]: list1[32],
            fieldnames[33]: list1[33],
            fieldnames[34]: list1[34],
            fieldnames[35]: list1[35],
            fieldnames[36]: list1[36],
            fieldnames[37]: list1[37],
            fieldnames[38]: list1[38],
            fieldnames[39]: list1[39],
            fieldnames[40]: list1[40],
            fieldnames[41]: list1[41],
            fieldnames[42]: list1[42],
            fieldnames[43]: list1[43],
            fieldnames[44]: list1[44],
            fieldnames[45]: list1[45],
            fieldnames[46]: list1[46],
            fieldnames[47]: list1[47],
            fieldnames[48]: list1[48],
            fieldnames[49]: list1[49],
            fieldnames[50]: list1[50],
            fieldnames[51]: list1[51],
            fieldnames[52]: list2[0],
            fieldnames[53]: list2[1],
            fieldnames[54]: list2[2],
            fieldnames[55]: list2[3],
            fieldnames[56]: list2[4],
            fieldnames[57]: list2[5],
            fieldnames[58]: list2[6],
            fieldnames[59]: list2[7],
            fieldnames[60]: list2[8],
            fieldnames[61]: list2[9],
            fieldnames[62]: list2[10],
            fieldnames[63]: list2[11],
            fieldnames[64]: list2[12],
            fieldnames[65]: list2[13],
            fieldnames[66]: list2[14],
            fieldnames[67]: list2[15],
            fieldnames[68]: list2[16],
            fieldnames[69]: list2[17],
            fieldnames[70]: list2[18],
            fieldnames[71]: list2[19],
            fieldnames[72]: list2[20],
            fieldnames[73]: list2[21],
            fieldnames[74]: list2[22],
            fieldnames[75]: list2[23],
            fieldnames[76]: list2[24],
            fieldnames[77]: list2[25],
            fieldnames[78]: list2[26],
            fieldnames[79]: list2[27],
            fieldnames[80]: list2[28],
            fieldnames[81]: list2[29],
            fieldnames[82]: list2[30],
            fieldnames[83]: list2[31],
            fieldnames[84]: list2[32],
            fieldnames[85]: list2[33],
            fieldnames[86]: list2[34],
            fieldnames[87]: list2[35],
            fieldnames[88]: list2[36],
            fieldnames[89]: list2[37],
            fieldnames[90]: list2[38],
            fieldnames[91]: list2[39],
            fieldnames[92]: list2[40],
            fieldnames[93]: value
        })
