class Make_Node():
    def __init__(self, feature_idx = None, threshold = None, left = None, right = None, variance = None, value = None):
        self.feature_idx = feature_idx
        self.threshold = threshold
        self.left = left
        self.right = right
        self.variance = variance
        self.value = value #For leaf node

class RegressionTree():
    def __init__(self, max_depth, min_split):
        self.root = None
        self.min_split = min_split
        self.max_depth = max_depth


    def split(self, df, feature_idx, threshold):
        left_child = np.array([sample for sample in df if sample[feature_idx] <= threshold])
        right_child = np.array([sample for sample in df if sample[feature_idx] > threshold])
        return left_child, right_child

    def train_squared_error(self, y, y_left, y_right):

        weight_left = len(y_left) / len(y)
        weight_right = len(y_right)/ len(y)
        variance = weight_left * np.var(y_left) + weight_right * np.var(y_right)

        #code says to subtract the parents error by the error fo the children. Not sure why we aren't just returning the variance of the children.
        return variance 



    def get_leaf(self, y):
        return np.mean(y)

    def best_feature(self, df, n_samples, n_features):
        best_split_dict = {}
        max_reduction = np.inf #Change variable to max_trained_squared_error?

        for feat_idx in range(n_features):
            feat_vals = df[:, feat_idx]
            threshold_options = np.unique(feat_vals)

            for threshold in threshold_options:
                left_child, right_child = self.split(df, feat_idx, threshold)
            
                if len(left_child) > 0 and len(right_child) > 0:
                    y, left_y, right_y = df[:, -1], left_child[:, -1], right_child[:, -1]

                    trained_squared_error = self.train_squared_error(y, left_y, right_y)

                    if trained_squared_error < max_reduction: #We want minimum variance. (If the trained_error function were to subtract frm the variance of the parent, flip to greater than).
                            best_split_dict["feature_idx"] = feat_idx
                            best_split_dict["threshold"] = threshold
                            best_split_dict["left_child"] = left_child
                            best_split_dict["right_child"] = right_child
                            best_split_dict["variance"] = trained_squared_error
                            max_reduction = trained_squared_error
        
        return best_split_dict


    def fit(self, X, y):
        df = np.concatenate((X, y), axis =1)
        self.root = self.build_tree(df)



    def build_tree(self, df, level = 0):
        X, y = df[:, :-1], df[:,-1]
        n_samples, n_features = np.shape(X)
        best_split = {} #hold all features of the split in  dict.
        if n_samples>= self.min_split and level <=self.max_depth:    #a1) Find the best feature for our tree to split on, if we haven't reached past our required tree size.

            best_split = self.best_feature(df, n_samples, n_features)

            if best_split['variance'] > 0:                          #a2) Split the tree based off this best feature into left and right subtrees
                left_tree = self.build_tree(best_split['left_child'], level +1)
                right_tree = self.build_tree(best_split['right_child'], level+1)

                return Make_Node(best_split['feature_idx'], best_split['threshold'], left_tree, right_tree, best_split['variance']) #a3) Make current split into Parent Node
        
        leaf = self.get_leaf(y)                                      #b1) if tree size has already been reached, (or reduction = 0), then create and return a Leaf Node.

        return Make_Node(value = leaf)


  

    def print_tree(self, tree=None, indent=" ", columns = None, level = 0, child = 'root' ):
            ''' function to print the tree '''
            self.columns = columns
            level+= 1

            if not tree:
                tree = self.root

            if tree.value is not None: #If there is value, this means it is a leaf node: return the regression value in this leaf node.
                print(' '*level*3, child, ': ',np.round(tree.value, 4))

            else: #Perform Pre-order traversal-- Root, Left, Right, (leaf).
                if self.columns is None: #If no column names were given, just print by column idx
                    print(f'{child}: X_{str(tree.feature_idx)}, "<=", {tree.threshold}, "?", {tree.variance}')
                    
                else:
                    print(' '*level*3, f'{child}: X_{self.columns[tree.feature_idx]}, "<=", {tree.threshold}, "?", {np.round(tree.variance, 4)}')

                    # print(indent, " |%sleft: " % (indent))
                    self.print_tree(tree.left, indent + indent, self.columns, level, child = 'left')
                    # print(indent, " |%sright :" % (indent), end)
                    self.print_tree(tree.right, indent + indent, self.columns, level, child = 'right')


    def make_prediction(self, x, root):

        if root.value:
            return root.value
        
        if x[root.feature_idx] < root.threshold:
            return self.make_prediction(x, root.left)

        else:
            return self.make_prediction(x, root.right)



    def predict(self, X):
        ''' function to predict a single data point '''
        
        predictions = [self.make_prediction(x, self.root) for x in X]
        return predictions



import pandas as pd
import numpy as np
from sklearn.datasets import load_boston;

X, y = load_boston(return_X_y = True);
data = load_boston();
df = pd.DataFrame(data.data, columns = data.feature_names);
df.head()

X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values.reshape(-1,1)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=41)

regressor = RegressionTree( 2, 2)
regressor.fit(X_train, Y_train)

print(regressor.predict([X_test[0]]))