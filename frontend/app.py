from flask import Flask, request, render_template
import requests
import base64

app = Flask(__name__)

API_URL = "https://sfcvvbp421.execute-api.us-east-1.amazonaws.com/predict"

class_mapping = {
    0: "Black Rot",
    1: "Esca (Black Measles)",
    2: "Leaf Blight",
    3: "Healthy"
}

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        file = request.files["image"]
        if file:
            img_data = base64.b64encode(file.read()).decode("utf-8")
            try:
                response = requests.post(API_URL, json={"image_base64": img_data})
                print("Response from API:", response.text)  # Debug line

                if response.status_code == 200:
                    result = response.json().get("prediction")
                    prediction = class_mapping.get(result, "Unknown")
                else:
                    prediction = f"Error: {response.status_code}"
            except Exception as e:
                prediction = f"Exception: {e}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
