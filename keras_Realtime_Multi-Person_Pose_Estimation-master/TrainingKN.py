import numpy
import pandas
from sklearn.neighbors import KNeighborsClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

seed = 7
numpy.random.seed(seed)

n_classes = 2

dataframe = pandas.read_csv("dataset_completo_dist_2.csv")

dataset = dataframe.values

X = dataset[:,0:93]
Y = dataset[:,93]

encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

X_train, X_test, y_train, y_test = train_test_split(X,dummy_y, test_size = 0.2)

print('Calcolo...')

classifier = KNeighborsClassifier(5)
history = classifier.fit(X_train, y_train)

y_score = classifier.predict(X_test)
print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(y_test, y_score)))

print("accuracy: %f" % accuracy_score(y_test, y_score))

result = []
result1 = []

for i in range(len(y_score)):
    if(y_score[i][0] == 1):
        result.append("fight")
    else:
        result.append("notfight")

for i in range(len(y_test)):
    if (y_test[i][0] == 1):
        result1.append("fight")
    else:
        result1.append("notfight")

print(confusion_matrix(result1,result))

#salvataggio e caricamento del modello
'''
# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(classifier, open(filename, 'wb'))


filename = 'finalized_model.sav'
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
predictions = loaded_model.predict(X_test)

print(predictions) 
'''