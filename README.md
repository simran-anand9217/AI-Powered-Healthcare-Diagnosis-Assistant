---
## AI-Powered Healthcare Diagnosis Assistant 🩺✨

An end-to-end Machine Learning web application that evaluates patient demographics, vitals, and selected symptoms to estimate risk tiers, output predictive diagnostic matches, and seamlessly route users to specialized healthcare professionals. 

> ⚠️ **CRITICAL DISCLAIMER:** This platform serves purely informational and educational metrics. It does not provide definitive medical diagnoses, clinical evaluations, or active prescriptions. Always consult a certified healthcare professional for medical advice.

---

## 🧱 Project Directory Structure

```text
AI_Healthcare_Diagnosis_Assistant/
│
├── dataset/
│   ├── symptoms.csv
│   ├── diseases.csv
│   ├── precautions.csv
│   ├── medications.csv
│   ├── doctors.csv
│   └── severity.csv
│
├── model/
│   ├── disease_model.pkl
│   ├── symptom_encoder.pkl
│   └── scaler.pkl
│
├── templates/
│   ├── index.html
│   ├── prediction.html
│   └── history.html
│
├── app.py
├── train_model.py
├── predict.py
├── database.py
├── requirements.txt
└── README.md
```
---
## ⚙️ How It Works (The Core Modules)

### 💻 1. Collecting Patient Info
The app starts with a straightforward dashboard where the user inputs their age, gender, weight, height, temperature, and checks off any symptoms they are currently experiencing from a list of 8 baseline options.

### 🔢 2. Smart Math & Feature Engineering
Before the AI even looks at the data, the app does some clever preprocessing:
* **Multi-Hot Encoding:** It turns a checklist of symptoms into a simple array of 1s and 0s (e.g., if you have a fever and cough, it transforms that into `[1, 1, 0, 0...]`).
* **BMI Calculator:** It takes the weight and height and instantly calculates Body Mass Index:
  $$BMI = \frac{\text{Weight (kg)}}{\text{Height (m)}^2}$$
* **Severity Scoring:** It checks the `severity.csv` file to calculate a custom severity score based on your active symptoms:
  $$\text{Severity Score} = \sum (\text{Active Symptom} \times \text{Symptom Weight})$$

### 🤖 3. The AI Prediction Engine
Instead of just guessing a single disease, the app uses a **Random Forest Classifier** to look at your symptoms and return the Top 3 most likely conditions along with percentage matches (for example: *Flu - 85%*, *Common Cold - 12%*, *Migraine - 3%*).

### 🚨 4. The Emergency Safe-Fail Trigger
Safety is baked directly into the code. Before the app even runs the AI model, it checks for red-flag combinations. If a user selects both **Chest Pain** and **Breathing Difficulty**, the app completely bypasses the prediction engine and throws a bright red, un-skippable Emergency Medical Alert Page telling them to call emergency services immediately.

### 🏥 5. Risk Triage & Recommendation Mapping
If there's no immediate emergency, the app calculates a total risk score based on age, temperature, and symptoms to place the user into a Low, Medium, or High risk tier. It then grabs matching data from our reference files to show:
* **The Right Specialist:** e.g., mapping a skin infection to a Dermatologist.
* **Precautions & Medicine Info:** General over-the-counter reference guidance and baseline lifestyle tips (like resting or staying hydrated).

### 💾 6. Local Diagnostic Ledger
Every time someone uses the application (and it's not a critical emergency), the details are saved to a local, lightweight **SQLite database**. Users can click "View Diagnosis History" at any time to see a neat history of previous runs.

---

## 🧰 The Tech Stack

* **Frontend UI:** HTML5, CSS3, Bootstrap 5 (clean, modern, and looks great on phones!)
* **Backend Server:** Flask (lightweight, fast, and easy to scale)
* **Security Protection:** Flask-WTF / CSRFProtect (keeps the app safe from malicious cross-site form submissions)
* **Data & AI Core:** Pandas, NumPy, Scikit-Learn (the golden standard for Python machine learning)
* **Storage Infrastructure:** SQLite3 (built-in SQL database that requires zero complex setup)
---
## 🚀 Step-by-Step Setup Guide

Ready to run it on your computer? Just follow these steps:

### 1. Download the Project
Clone the repository using Git and jump into the directory:

```bash
git clone [https://github.com/YOUR_USERNAME/AI_Healthcare_Diagnosis_Assistant.git](https://github.com/YOUR_USERNAME/AI_Healthcare_Diagnosis_Assistant.git)
cd AI_Healthcare_Diagnosis_Assistant
```
### 2. Set Up a Virtual Environment

It's always a good idea to keep your Python packages isolated so they don't conflict with other projects:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the Dependencies
Use the requirements.txt file to install everything your app needs in one go:

```Bash
pip install -r requirements.txt
```

### 4. Create Your Security Key
We use CSRF security tokens to keep forms safe. Create a text file named exactly .env in the root folder of the project and add a secret key:

```Plaintext
SECRET_KEY=put_any_random_long_string_of_numbers_and_letters_here
```
> 💡 **Note:** If you skip this step, the app has a built-in fallback key so it won't crash!

### 5. Train the AI Model

Before launching the website, we need to create our datasets and train the AI. Run this script once:

```bash
python train_model.py
```

### 6. Start the Web Server

Now, let's boot up the web application:

```bash
python app.py
```

<img width="1126" height="145" alt="image" src="https://github.com/user-attachments/assets/f62a724e-f46b-4797-bb15-0801bee44050" />

Open your favorite web browser and head over to: http://127.0.0.1:5000 🎉

<img width="707" height="570" alt="image" src="https://github.com/user-attachments/assets/c1d04576-532a-4726-85af-a08857bbad46" />

---

** For Example -->

<img width="975" height="905" alt="image" src="https://github.com/user-attachments/assets/f43f1bf9-1354-465f-b1a6-2126dc00231c" />


---
## 🛡️ Privacy & Safety

* **Completely Local:** Your health data never leaves your machine. The SQL database and the AI model run entirely on your local computer, meaning total privacy.

<img width="1505" height="427" alt="image" src="https://github.com/user-attachments/assets/36b0ae94-5fac-4335-a689-38c234eeee25" />

  
* **Smart Overrides:** Life-threatening symptom combinations immediately jump to emergency screens, putting user safety above machine learning numbers.

---

## 🔮 Wrapping Up & What's Next

### Conclusion
Building this app shows how powerful machine learning can be when combined with smart, human-focused rules. By focusing on probabilities and specialist routing rather than trying to pretend to be a real doctor, the app gives users helpful, data-driven personal health awareness safely and responsibly.

### The Roadmap Ahead (Future Ideas)
This project is just getting started! Here are a few features planned for the future:

* **AI Health Chatbot:** Integrating an offline Large Language Model (LLM) using RAG so users can talk casually about how they feel instead of just clicking checkboxes.
* **Skin Condition Scanning:** Adding a computer vision model (CNN) so users can securely upload a photo of a rash or bug bite for an instant risk analysis.
* **PDF Report Downloads:** Letting users export their results into a clean, password-protected PDF that they can print out and hand directly to their doctor.
* **EHR Interoperability:** Upgrading our database layouts to match international medical data standard formats (like FHIR) so it can securely talk to real hospital software ecosystems down the line.
