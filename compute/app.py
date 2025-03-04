from flask import Flask, request
from cloud.s3 import test
app = Flask(__name__)

@app.route("/receive_model", methods=["POST"])
def receive_model():
    data = request.json
    model_name = data.get("model_name", "Unknown Model")
    print(f"Received model: {model_name}")
    test()
    return {"status": "success", "received_model": model_name}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)