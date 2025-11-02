from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("liquidity_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        trading_volume = float(request.form['trading_volume'])
        transaction_pattern = float(request.form['transaction_pattern'])
        exchange_listing = float(request.form['exchange_listing'])
        social_media_activity = float(request.form['social_media_activity'])

        input_data = np.array([[trading_volume, transaction_pattern, exchange_listing, social_media_activity]])

        prediction = model.predict(input_data)[0]

        return render_template(
            'index.html',
            prediction_text=f"Predicted Liquidity Ratio: {prediction:.6f}"
        )

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)