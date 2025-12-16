import json

import requests

# TODO: send a GET using the URL http://127.0.0.1:8000  (Done!)
r = requests.get("http://127.0.0.1:8000") # Your code here (Done!)

# TODO: print the status code (Done!)
print("GET request status code:", r.status_code)
# TODO: print the welcome message (Done!)
print("GET request welcome message:", r.json())



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above (Done!)
r = requests.post("http://127.0.0.1:8000/data/", json=data) # Your code here (Done!)

# TODO: print the status code (Done!)
print("POST request status code:", r.status_code)
# TODO: print the result (Done!)
print("POST request result:", r.json())