from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertForSequenceClassification

import tensorflow as tf
import json
import numpy as np
import warnings
warnings.filterwarnings("ignore")

the model and tokenizer is initialised outside so that it will only be called once
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
loaded_model = TFDistilBertForSequenceClassification.from_pretrained("./static/models/bert_model")

def bert_model(sentence):
    global tokenizer
    global loaded_model

    predict_input = tokenizer.encode(sentence,
                                    truncation=True,
                                    padding=True,
                                    return_tensors="tf")

    tf_output = loaded_model.predict(predict_input)[0]

    tf_prediction = tf.nn.softmax(tf_output, axis=1)
    labels = ['Negative','Positive']
    label = tf.argmax(tf_prediction, axis=1)
    label = label.numpy()
    return labels[label[0]]


def vader_model(sentence):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)["compound"]
    if score >= 0:
        return "Positive"
    else: 
        return "Negative"