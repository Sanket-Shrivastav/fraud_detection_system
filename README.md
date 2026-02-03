# Fraud Detection System

## Overview
A web-based Fraud Detection System using Python, Flask, and Machine Learning. The system identifies suspicious financial transactions in real-time, helping reduce risks for banks and payment platforms.

---

## How to Run the Project

Follow these steps exactly:

### Step 1: Clone the repository
Open CMD and run:

```cmd
git clone <your-github-repo-link>
cd fraud_detection_system

Step 2: Create a Virtual Environment
python -m venv venv

Step 3: Activate the Virtual Environment
venv\Scripts\activate
Your CMD prompt should now show (venv) at the start.

Step 4: Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

Step 5: Install Dependencies
pip install -r requirements.txt
This will install Flask, pandas, scikit-learn, numpy, and other required libraries.

Step 6: Run the Application
python app.py
You should see something like:

 * Running on http://127.0.0.1:5000

Step 7: Open in Browser
Open your browser and go to:

http://127.0.0.1:5000
Enter transaction details → Click Check Transaction → See the prediction.

Project Structure
fraud_detection_system/
│
├── app.py                 # Main Flask app
├── requirements.txt       # Dependencies
├── README.md              # Project description (this file)
├── SRS.docx               # Software Requirements Specification
├── templates/
│   └── index.html         # HTML page
├── static/
│   └── style.css          # CSS for styling
└── venv/                  # Virtual environment
Technologies Used
Python 3.10+
Flask
Scikit-learn
pandas, numpy

Author

SANKET RAVINDRAKUMAR SHRIVASTAV
