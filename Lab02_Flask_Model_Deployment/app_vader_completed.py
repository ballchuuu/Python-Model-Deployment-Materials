from flask import Flask, jsonify, request, render_template, json

app = Flask(__name__)
   
from utils import vader_model
    
#### GET REQUEST ####
@app.route("/get_model_details/", methods = ["GET"])
def get_model_details():

    # How to access the get request via browser: http://localhost:5000/get_model_details?model_type=Vader

    model_details = {"Vader": "here is a vader model",
                      "Bert": "here is a bert model"}

    # checks if model_type parameter is in request.args (i.e. data input)
    if "model_type" in request.args:
        chosen_model = request.args["model_type"]

        if chosen_model in model_details:
            return jsonify(model_details[chosen_model])
        else:
            return jsonify("This model doesnt exist in our database")
           
    return jsonify("Please input a valid key value pair in the format of {'model_type': 'Vader'}")

#### POST REQUEST WITH FILE UPLOAD ####
@app.route("/model_inference_files/", methods = ["POST"])
def model_inference_files():
    
    # csv file format
    if "file" in request.files:
        data = request.files["file"].read().decode("utf8")
    
        # check if the file is empty
        if data != "":
            # split the data into sentences
            sentences = [i.strip() for i in data.split("\n")]

            # perfom inference
            return jsonify([{"text": i, "sentiment_predicted": vader_model(i)} for i in sentences])
        else:
            return jsonify("Please provide data in your file.")

    return jsonify("Please provide your file in the following format {'file': open('test-data.csv', 'r')}")

#### RENDERING A SIMPLE INTERFACE WITH POST & GET REQUEST ####
@app.route('/') # Homepage
def home():
    return render_template('index.html')

@app.route("/predict_html/", methods=["POST"])
def predict_html():

    params = request.form
    model_type = params["model_type"]
    text = params["text"]
    prediction = vader_model(text)

    return render_template("index.html", prediction = f"Prediction Sentiment: {prediction}",
                                        model_type = f"Model Type: {model_type}",
                                        text = f"Input text: {text}")

if __name__ == "__main__":
    app.run(debug=True)
	