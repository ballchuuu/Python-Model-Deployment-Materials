from flask import Flask, jsonify, request, render_template, json

app = Flask(__name__)

from utils import vader_model, bert_model   
from models import Lexicon_dictionary, Sentiment_score 
    
#### GET REQUEST ####
@app.route("/get_model_details/", methods = ["GET"])
def get_model_details():
    model_details = {
        "Vader": "VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.",
        "DistilBERT": "DistilBERT, a smaller and faster version of BERT is used as the pre-trained model. The sentiment analysis dataset used for transfer learning is the IMDB movie review dataset. The training and prediction code has been adapted from the following link: https://blog.doit-intl.com/performing-surprisingly-easy-sentiment-analysis-on-google-cloud-platform-fc26b2e2b4b"}
    
    if "model_type" in request.args:
        chosen_model = request.args["model_type"]
        if chosen_model in model_details:
            return jsonify(model_details[chosen_model])
        else:
            return jsonify("This model does not exist! Please input a valid model (i.e. Vader/DistilBERT).")
    else:
        return jsonify("Please input a json in the following format {'model_details': 'Vader'}")


#### POST REQUEST WITH FILE UPLOAD ####
@app.route("/model_inference_files/", methods = ["POST"])
def model_inference_files():

    try:
        if "file" in request.files:
            model_data = request.form
            model_type = model_data["model_type"]

            # read the data file
            data = request.files["file"].read().decode("utf8")

            # check if the data is empty
            if data != '':
        
                sentences = [i.strip() for i in data.split("\n")]

                if model_type == "Vader":
                    return jsonify([{"text": i,"sentiment": vader_model(i)} for i in sentences])
                elif model_type == "DistilBERT":
                    return jsonify([{"text": i, "sentiment": bert_model(i)} for i in sentences])
                else:
                    return jsonify("Please provide a valid model type (i.e. Vader and DistilBERT)!")

          
        return jsonify("Please provide a valid file using the following format: {'file': open('test_data.csv' ,'r')}")

    except Exception as e:
        return(str(e))
        

#### RENDERING A SIMPLE INTERFACE WITH POST & GET REQUEST ####
@app.route('/') # Homepage
def home():
    return render_template('index.html')

@app.route("/predict_html/", methods=["POST"])
def predict_html():

    params = request.form
    # check if a json is provided for a single sentence prediction
    if "text" in params and "model_type" in params:

        model_type = params["model_type"]
        text = params["text"]

        # do single sentence prediction for vader model
        if model_type == "Vader":
            prediction = vader_model(text)
        elif model_type == "DistilBERT":
            prediction = bert_model(text)
        else:
            prediction = "Please provide a valid model type (i.e. Vader and DistilBERT)!"
        
        return render_template('index.html', 
                                prediction = f"Predicted sentiment: {prediction}", 
                                model_type = f"Chosen model: {model_type}", 
                                text = f"Input text: {text}") # rendering the predicted result


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
	