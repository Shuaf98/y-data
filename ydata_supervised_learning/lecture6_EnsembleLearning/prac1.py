import numpy as np
import pandas as pd

from sklearn.datasets import load_boston
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

X, y = load_boston(return_X_y = True);
data = load_boston();
df = pd.DataFrame(data.data, columns = data.feature_names);

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)


class CustomGB():
    def __init__(self, n_estimators, learning_rate):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.weights = None
        self.trees = [] #F(x)
        self.prev_predict = None
         

    def fit(self, X, y):
        self.X = np.array(X)
        self.y = np.array(y)

        self.average_leaf = np.mean(self.y)
        self.prev_predict = np.mean(self.y)
        self.trees.append(self.average_leaf) #F0(X)
        
        for m in range(1, self.n_estimators +1): #I think plus 1
            residuals = self.y - self.prev_predict[-1]
            tree = DecisionTreeRegressor(max_depth = 10 )
            tree.fit(self.X, residuals)
            self.trees.append(tree) #Is this where I should append the tree?

            residual_prediction = tree.predict(X) 
            gradient_prediction = self.prev_predict[-1] +(self.learning_rate * residual_prediction)
            # print(gradient_prediction)


            self.prev_predict = np.array(gradient_prediction)

    def predict(self, X):
        predictions_sum =  []
        for tree in self.trees[1:]:
            predictions_sum.append(self.learning_rate * tree.predict(X))
        predict = self.average_leaf + np.sum(predictions_sum, axis = 0)
        return predict

from sklearn.metrics import r2_score, mean_squared_log_error 
GB = CustomGB(1000, 0.01)
GB.fit(x_train, y_train)
r2_score(y_train, GB.predict(x_train))