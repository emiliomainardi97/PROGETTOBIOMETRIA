import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline

from sklearn.svm import SVC

from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score


dataset = pd.read_csv('dataset_completo_dist_2.csv')
dataset.head()
#divisione in train test e test set
train_set, test_set = train_test_split(dataset, test_size=0.2, random_state=42)

#divido i dati di train dalle loro etichette
train_set_copy=train_set.copy()
datisenzalabel=train_set_copy.drop(['label'],axis=1)
labeldata=train_set['label']

#creo un classificatore svm

polynomialclassifierkernel = Pipeline([

    ("svm_clf", SVC(kernel="poly", degree=3, coef0=1, C=100))
])

#allenamento classificatore svm
polynomialclassifierkernel.fit(datisenzalabel,labeldata)

#accuracy con la cross validation sui dati di training
score=cross_val_score(polynomialclassifierkernel, datisenzalabel, labeldata, cv=5, scoring="accuracy")
print("Accuracy con la cross-validation")
score.mean()

#separo i dati di test dalle etichette
test_set_copy=test_set.copy()
testsenzalabel=test_set_copy.drop(['label'],axis=1)
labeldatatest=test_set['label']
#predizione
predizione=polynomialclassifierkernel.predict(testsenzalabel)
#accuracy sui dati di test
print("Accuracy sui dati di test")
accuracy_score(predizione,labeldatatest)