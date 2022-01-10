import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_boston
from sklearn.tree import DecisionTreeRegressor
X, y = load_boston(return_X_y = True);
data = load_boston();
df = pd.DataFrame(data.data, columns = data.feature_names);
df.head()


class Tree():
    def __init__(self, dt, X, y, columns):
        self.dt = dt
        self.X = X
        self.y = y
        self.columns = columns

class TreeEnsemble():
    def __init__(self, n_trees, sample_sz, n_features, min_leaf):
        self.n_trees = n_trees
        self.sample_sz = sample_sz
        self.n_features = n_features
        self.min_leaf = min_leaf

    def fit(self, X, y):    
        df = pd.DataFrame(np.append(X, y.reshape(-1,1), axis =1))
        self.estimators = []
        for i in range(self.n_trees):
        #Random sampling, with replacement, of the data.
            # samples = np.random.choice(df.sha, self.sample_sz, replace = True)
            sample = df.sample(self.sample_sz, replace= True)

            X = sample.iloc[:, :-1]
            y = sample.iloc[:, -1]
        #Random sampling of the features
            X = X.sample(self.n_features, axis = 1)
            columns = X.columns
           
        #Create tree (with min_leaf)
            dt = DecisionTreeRegressor(min_samples_leaf= self.min_leaf).fit(X, y)

            tree = Tree(dt = dt, X = X, y = y, columns = columns)
            
        #add tree to the total amount of classifiers.
            self.estimators.append(tree)


    def predict(self, X):
        
        predictions = []
        for tree in self.estimators:
            X = X[:, tree.columns]
            
            predictions.append(tree.dt.predict(X))
        
        return np.mean(predictions, axis = 1)

    def oob_mse(self):
        pass

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)

rf = TreeEnsemble(50, 100, 5, 1)
rf.fit(x_train,y_train)

rf.predict(x_test)