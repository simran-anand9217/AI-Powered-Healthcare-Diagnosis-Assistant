from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv
from predict import evaluate_patient
from database import init_db, log_prediction, get_history

load_dotenv()

app = Flask(__name__)
SECRET_KEY_ENV = 'SECRET_KEY'
secret_key = os.environ.get(SECRET_KEY_ENV)
if not secret_key:
    raise ValueError(f'{SECRET_KEY_ENV} environment variable is not set')
app.config[SECRET_KEY_ENV] = secret_key
csrf = CSRFProtect(app)

# Guarantee operational database setup
if not os.path.exists('database.db'):
    init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Safely extract input fields (Module 1)
        patient_profile = {
            'age': request.form.get('age'),
            'gender': request.form.get('gender'),
            'weight': request.form.get('weight'),
            'height': request.form.get('height'),
            'temperature': request.form.get('temperature'),
            'symptoms': request.form.getlist('symptoms')
        }
        
        result = evaluate_patient(patient_profile)
        
        if result.get('emergency'):
            return render_template('prediction.html', emergency=True, message=result['message'])
            
        # Write operational metrics directly into histories tracking index table
        log_prediction(
            age=patient_profile['age'],
            gender=patient_profile['gender'],
            disease=result['predictions'][0]['disease'],
            probability=result['predictions'][0]['probability'],
            risk_level=result['risk_level'],
            specialist=result['specialist']
        )
        
        return render_template('prediction.html', emergency=False, result=result, profile=patient_profile)
        
    return render_template('index.html')

@app.route('/history', methods=['GET'])
def history():
    records = get_history()
    return render_template('history.html', records=records)

if __name__ == '__main__':
    app.run(port=5000)