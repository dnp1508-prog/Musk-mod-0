'''
Dadas las siguientes clases con el output de sus
respectivos métodos, crea una interfaz formal
que las implemente.
'''
import abc
class SVM(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def preprocess_data(self, data = None, y = None):
        pass
    @abc.abstractmethod
    def fit(self):
        pass
    @abc.abstractmethod
    def predict(self):
        pass

class DecisionTree(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def preprocess_data(self, data = None, y = None):
        pass
    @abc.abstractmethod
    def fit(self):
        pass
    def predict(self):
        pass
class SVM(SVM):
    def preprocess_data(self, data = None, y = None):
        print("Preprocessing data at SVM")
    def fit(self):
        print("Training at SVM")
    def predict(self):
        print("Evaluating at SVM")
class DecisionTree(DecisionTree):
    def preprocess_data(self, data = None, y = None):
        print("Preprocessing data at DecisionTree")
    def fit(self):
        print("Training at DecisionTree")
    def predict(self):
        print("Evaluating at DecisionTree")
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