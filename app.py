from flask import Flask, request, jsonify
import joblib
import os
import numpy as np
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

# Load model and scaler (ensure the files exist)
try:
    model = joblib.load('best_model.pkl')  # Replace with the correct model path
    scaler = joblib.load('scaler.pkl')  # Replace with the correct scaler path
except FileNotFoundError:
    print("Error: Model or Scaler file not found! Train the model first.")
@app.route('/')
def home():
    return "Flask API is Running! Use the /predict endpoint."
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        rd_spend = data.get('rdSpend', 0)
        admin_spend = data.get('adminSpend', 0)
        marketing_spend = data.get('marketingSpend', 0)

        # Prepare the input data for the model
        input_data = np.array([[rd_spend, admin_spend, marketing_spend]])

        # Scale the input data
        scaled_input = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(scaled_input)

        # Return the prediction as JSON
        return jsonify({'predictedProfit': float(prediction[0])})  # Convert to float for JSON compatibility

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
