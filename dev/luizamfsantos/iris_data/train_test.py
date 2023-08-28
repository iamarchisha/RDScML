import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import CategoricalNB

### Model #1 Decision Tree
def decision_tree(train_X, val_X, train_y, val_y):
    classifier = DecisionTreeClassifier(random_state=1)
    classifier.fit(train_X,train_y)
    predictions = classifier.predict(val_X)
    return mean_absolute_error(predictions, val_y)

### Model #2 Random Forest
def forest(train_X, val_X, train_y, val_y):
    classifier = RandomForestRegressor(random_state=1)
    classifier.fit(train_X,train_y)
    predictions = classifier.predict(val_X)
    return mean_absolute_error(predictions, val_y)

### Model #3 Categorical Naive Bayes
def bayes(train_X, val_X, train_y, val_y):
    classifier = CategoricalNB(force_alpha=True)
    classifier.fit(train_X,train_y)
    predictions = classifier.predict(val_X)
    return mean_absolute_error(predictions, val_y)


### Choosing the best model
def find_smallest_key(dict_models):
    smallest_float = float('inf')
    smallest_key = None

    for key, value in dict_models.items():
        if value < smallest_float:
            smallest_float = value
            smallest_key = key

    return smallest_key
