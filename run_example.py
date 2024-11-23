# check if app working

import requests
import json

# URL where the Flask API is running
url = 'http://localhost:9696/predict'

# Example input data (same format as used in training)
data = {
    "age": 35,
    "workclass": "Private",
    "education": "Bachelors",
    "marital-status": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States"
}

# Send a POST request with the input data
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Convert response to JSON and print
    result = response.json()
    print("Prediction:", result['prediction'])
    print("Probability:", result['probability'])
else:
    print("Error:", response.status_code, response.text)