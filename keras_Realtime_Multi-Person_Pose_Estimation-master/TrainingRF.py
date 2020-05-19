import numpy
import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from keras.utils import np_utils
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt


import pickle


seed = 7
numpy.random.seed(seed)

n_classes = 2

dataframe = pandas.read_csv("dataset_completo_dist_2.csv")

dataset = dataframe.values

X = dataset[:,0:93]
y = dataset[:,93]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

classifier = RandomForestClassifier(n_estimators=20, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
plt.show()
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

kfold = KFold(n_splits=25, shuffle=True, random_state=0)

accuracies = cross_val_score( estimator = classifier , X = X_train, y = y_train, cv = kfold)

print(accuracies.mean())


# save the model to disk
filename = 'finalized_modelRF.sav'
pickle.dump(classifier, open(filename, 'wb'))


filename = 'finalized_modelRF.sav'
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
predictions = loaded_model.predict(X_test)

print(predictions)


titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(classifier, X_test, y_test,
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)
    plt.show()

