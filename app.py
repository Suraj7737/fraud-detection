from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

pipe = joblib.load('fruad_detection_pipeline.pkl')

# Ensure cross-version compatibility for LogisticRegression (scikit-learn < 1.7 compatibility)
for _, step in getattr(pipe, 'steps', []):
    if hasattr(step, '__class__') and 'LogisticRegression' in step.__class__.__name__:
        if not hasattr(step, 'multi_class'):
            step.multi_class = 'auto'


@app.route('/')
def index():
    return send_from_directory('.', 'fraud-detection.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        df = pd.DataFrame([{
            'amount':         float(data['amount']),
            'oldbalanceOrg':  float(data['oldbalanceOrg']),
            'newbalanceOrig': float(data['newbalanceOrig']),
            'oldbalanceDest': float(data['oldbalanceDest']),
            'newbalanceDest': float(data['newbalanceDest']),
            'type':           data['type'],
        }])

        # Ensure columns are in the same order the model was trained on

        prediction = pipe.predict(df)[0]
        probability = pipe.predict_proba(df)[0][1]

        return jsonify({
            'isFraud': int(prediction),
            'fraudProbability': round(float(probability) * 100, 2),
            'verdict': 'FRAUD' if prediction == 1 else 'LEGITIMATE'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)