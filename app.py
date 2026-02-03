from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

app = Flask(__name__)

# Train model (run once)
data_file = os.path.join("data", "transactions.csv")
df = pd.read_csv(data_file)

X = df[['Amount','OldBalance','NewBalance']]
y = df['IsFraud']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Load model
with open("model.pkl", "rb") as f:
    clf = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    amount = float(data['amount'])
    old_balance = float(data['old_balance'])
    new_balance = float(data['new_balance'])

    prediction = clf.predict([[amount, old_balance, new_balance]])[0]
    result = "Fraudulent" if prediction == 1 else "Legitimate"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
