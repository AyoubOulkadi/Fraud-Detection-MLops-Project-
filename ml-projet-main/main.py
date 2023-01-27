import os
from flask_cors import CORS, cross_origin
# Import libraries
import numpy as np
import json
from flask import Flask, request, jsonify
import tensorflow as tf
app = Flask(__name__)
# Load the model
model = tf.keras.models.load_model('my_model', compile=False)
model.compile(optimizer="adam", loss="binary_crossentropy",
              metrics=["accuracy"])


@app.route('/api', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.json
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict(np.array(data['exp']).reshape(1, 14))
    # # Take the first value of prediction
    output = prediction[0]
    return str(output)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=os.getenv("PORT", default=5000))
