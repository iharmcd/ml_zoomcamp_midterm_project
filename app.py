import pickle
from flask import Flask, request, jsonify
import xgboost as xgb
import numpy as np

app = Flask(__name__)

# Load the trained model and DictVectorizer
with open('xgb_model.pkl', 'rb') as model_file:
    model_XGB = pickle.load(model_file)

with open('dv_scaler.pkl', 'rb') as f:
    data = pickle.load(f)
    dv = data['dict_vectorizer']
    scaler = data['scaler']

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.json

    X_new = dv.transform(data)
    X_new_scaled = scaler.transform(X_new)

    # Convert to DMatrix for XGBoost prediction
    dmatrix = xgb.DMatrix(X_new_scaled, feature_names=dv.feature_names_)

    # Make prediction
    prediction_proba = model_XGB.predict(dmatrix)
    prediction = int(prediction_proba >= 0.5)  # Threshold at 0.5

    # Return prediction as JSON
    response = {
        'prediction': prediction,
        'probability': float(prediction_proba)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
