# Import Necessary Libraries
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import CategoricalNB

def decision_tree(train_X, val_X, train_y, val_y):
    """
    ### Model #1 Decision Tree

    Parameters:
    -----------
    train_X : array-like
        The feature matrix of the training dataset.

    val_X : array-like
        The feature matrix of the validation dataset.

    train_y : array-like
        The target values of the training dataset.

    val_y : array-like
        The target values of the validation dataset.

    Returns:
    --------
    float
        The Mean Absolute Error (MAE) between the predicted values and the actual values in the validation dataset.


    Function Description:
    ---------------------
    1. Initialization: Inside the function, a Decision Tree classifier is initialized with a specified random state to ensure reproducibility.
    2. Model Training: The classifier is trained using the training data (`train_X` and `train_y`) to learn the underlying patterns in the data.
    3. Predictions: The trained model is used to make predictions on the validation data (`val_X`), and these predictions are stored in the `predictions` variable.
    4. Evaluation: The function calculates the Mean Absolute Error (MAE) by comparing the predicted values with the actual values in the validation dataset (`val_y`).

       """
    classifier = DecisionTreeClassifier(random_state=1)
    classifier.fit(train_X, train_y)
    predictions = classifier.predict(val_X)
    return mean_absolute_error(predictions, val_y)


def forest(train_X, val_X, train_y, val_y):
    """
    Model #2 Random Forest

    Parameters:
    -----------
    train_X : array-like
        The feature matrix of the training dataset.

    val_X : array-like
        The feature matrix of the validation dataset.

    train_y : array-like
        The target values of the training dataset.

    val_y : array-like
        The target values of the validation dataset.

    Returns:
    --------
    float
        The Mean Absolute Error (MAE) between the predicted values and the actual values in the validation dataset.


    Function Description:
    ---------------------
    1. Initialization: Inside the function, a Random Forest Regressor is initialized with a specified random state to ensure reproducibility.
    2. Model Training: The regressor is trained using the training data (`train_X` and `train_y`) to learn the underlying patterns in the data.
    3. Predictions: The trained model is used to make predictions on the validation data (`val_X`), and these predictions are stored in the `predictions` variable.
    4. Evaluation: The function calculates the Mean Absolute Error (MAE) by comparing the predicted values with the actual values in the validation dataset (`val_y`).

    """
    classifier = RandomForestRegressor(random_state=1)
    classifier.fit(train_X, train_y)
    predictions = classifier.predict(val_X)
    return mean_absolute_error(predictions, val_y)


def bayes(train_X, val_X, train_y, val_y):
    """
    Model #3 Categorical Naive Bayes

    Parameters:
    -----------
    train_X : array-like
        The feature matrix of the training dataset.

    val_X : array-like
        The feature matrix of the validation dataset.

    train_y : array-like
        The target values of the training dataset.

    val_y : array-like
        The target values of the validation dataset.

    Returns:
    --------
    float
        The Mean Absolute Error (MAE) between the predicted values and the actual values in the validation dataset.

    Function Description:
    ---------------------
    1. Initialization: Inside the function, a Categorical Naive Bayes classifier is initialized with the `force_alpha=True` argument to automatically compute and apply Laplace smoothing.
    2. Model Training: The classifier is trained using the training data (`train_X` and `train_y`) to learn the underlying patterns in the data.
    3. Predictions: The trained model is used to make predictions on the validation data (`val_X`), and these predictions are stored in the `predictions` variable.
    4. Evaluation: The function calculates the Mean Absolute Error (MAE) by comparing the predicted values with the actual values in the validation dataset (`val_y`).
    Note:
    -----
    - The `force_alpha=True` argument was used because my dataset is small. 
    """
    classifier = CategoricalNB(force_alpha=True)
    classifier.fit(train_X, train_y)
    predictions = classifier.predict(val_X)
    return mean_absolute_error(predictions, val_y)



def find_smallest_key(dict_models):
    """
    Choosing the Best Model

    Parameters:
    -----------
    dict_models : dict
        A dictionary containing model names as keys and associated evaluation scores as values.

    Returns:
    --------
    str or None
        The name of the model with the smallest evaluation score, or None if the input dictionary is empty.
        
    Function Description:
    ---------------------
    1. Initialization: Inside the function, variables `smallest_float` and `smallest_key` are initialized. `smallest_float` is set to positive infinity, 
       and `smallest_key` is set to None.
    2. Model Selection: The function iterates through the dictionary `dict_models`, comparing the evaluation scores. 
       It updates `smallest_float` and `smallest_key` whenever a smaller score is encountered.
    3. Return: Finally, the function returns the name of the model with the smallest evaluation score (`smallest_key`) or None if the input dictionary is empty.

    Note:
    -----
    - This function is useful for automating the selection of the best model based on evaluation scores, such as Mean Absolute Error (MAE) or other metrics.
    - It assumes that `dict_models` is a dictionary with model names as keys and numeric evaluation scores as values.
    """
    smallest_float = float('inf')
    smallest_key = None

    for key, value in dict_models.items():
        if value < smallest_float:
            smallest_float = value
            smallest_key = key

    return smallest_key
