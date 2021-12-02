import numpy as np
import pandas as pd
import matplotlib as plt


def true_boundary_voting_pred(wealth, religiousness):
  return religiousness-0.1*((wealth-5)**3-wealth**2+(wealth-6)**2+80)

def generate_data(m, seed=None):
  # if seed is not None, this function will always generate the same data
  np.random.seed(seed) 
  
  X = np.random.uniform(low=0.0, high=10.0, size=(m,2))
  y = np.sign(true_boundary_voting_pred(X[:,0], X[:,1]))
  y[y==0] = 1 #sign of 0 is defined as 1 for this case
  samples_to_flip = np.random.randint(0,m//10)
  flip_ind = np.random.choice(m, samples_to_flip, replace=False)
  y[flip_ind] = -y[flip_ind] #turn into negative values. So positives equal negative, and negatives = positives.
  y[y==-1] = 0 #afterwars, turn the negative ones into 0 (my own addition, to be consistent with the regualr knn algorithm)
  return X, y

def pred_y(x, y, n):
    knn = kNNClassifier(n)
    knn.fit(x, y)
    return knn.predict(x)

def error(y, pred_y):
    TP = len(y[(y == 1) & (pred_y ==1)])
    TN = len(y[(y == 1) & (pred_y ==1)])
    FP = len(y[(y == 0) & (pred_y == 1)])
    FN = len(y[(y == 1) & (pred_y == 0)])

    recall = TP / (TP + FN)
    precision = TP / (TP + FP)
    acc = (TP + TN) / (TP + TN + FP + FN)
    F1 = (2*precision*recall) / (precision + recall)

    return acc/F1


np.random.seed(5)
X, y = generate_data(1000)

x_train = X[:600]
y_train = y[:600]
x_valid = X[600:800]
y_valid = y[600:800]
x_test = X[800:]
y_test = y[800:]

k_vals = np.arange(1,16,1)
train_vals = []
valid_vals = []
for k in k_vals:
    pred_y_train = pred_y(x_train, y_train, k)
    train_error = error(y_train, pred_y_train)
    train_vals.append(train_error)

    pred_y_train = pred_y(x_valid, y_valid, k)
    valid_error = error(y_valid, pred_y_train)
    valid_vals.append(train_error)

plt.plot(k_vals, train_vals)
plt.plot(k_vals, valid_vals)