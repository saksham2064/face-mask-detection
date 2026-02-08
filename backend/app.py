from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/detect-mask")
def detect_mask():
    result = random.choice(["Mask", "No Mask"])
    confidence = round(random.uniform(0.7, 1.0), 2)
    return jsonify({"label": result, "confidence": confidence})

if __name__ == "__main__":
    app.run(debug=True)
