import pandas as pd
import glob
import sys
import matplotlib.pyplot as plt

path = ('DATASET/DATASET_DIST') # use your path
all_files = glob.glob(path + "/*.csv")
li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

result = pd.concat(li, axis=0, ignore_index=True, sort = False) #per combinare più files uno sotto l' altro

result.to_csv('DATASET/DATASET_DIST/dataset_completo_dist.csv', index=False)

