'''
Repite el ejercicio anterior esta vez creando una
interfaz informal.
'''

class SVM():
    def preprocess_data(self, data = None, y = None):
        print("Preprocessing data at SVM")
    def fit(self):
        print('Training at SVM')
    def predict(self):
        print('Evaluating at SVM')

class DecisionTree():
    def preprocess_data(self, data = None, y = None):
        print("Preprocessing data at DecisionTree")
    def fit(self):
        print('Training at DecisionTree')
    def predict(self):
        print('Evaluating at DecisionTree')
svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()
dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()
'''
Preprocessing data at SVM
Training at SVM
Evaluating at SVM
Preprocessing data at DecisionTree
Training at DecisionTree
Evaluating at DecisionTree
'''
