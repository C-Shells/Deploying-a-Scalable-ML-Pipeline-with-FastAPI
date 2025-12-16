# import pytest
# TODO: add necessary import (Done!)
import pandas as pd
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("data/census.csv")
train, test = train_test_split(data, test_size=0.20, random_state=42)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)
X_test, y_test, _, _ = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb
)


# TODO: implement the first test. Change the function name and input as needed
def test_train_model_is_random_forest_classifier():
    """
    # Testing that the train_model function returns a RandomForestClassifier
    """
    # Your code here
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model is not RFC"


# TODO: implement the second test. Change the function name and input as needed (Done!)
def test_inference_shape_value():
    """
    # Testing that the inference function returns predictions of
    # correct shape and values, 0/1.
    """
    # Your code here
    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    assert len(preds) == len(y_test), (
        "Inference output shape does not match expected shape"
    )
    assert set(preds).issubset({0, 1}), "Inference output contains unexpected values"


# TODO: implement the third test. Change the function name and input as needed (Done!)
def test_compute_model_metrics():
    """
    # Testing that the compute_model_metrics function returns correct metrics
    """
    # Your code here
    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)
    assert isinstance(precision, float), "Precision is not a float"
    assert isinstance(recall, float), "Recall is not a float"
    assert isinstance(fbeta, float), "Fbeta is not a float"
