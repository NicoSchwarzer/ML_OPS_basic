# 1. Library imports
import pandas as pd
import numpy as np 
#import torch
import transformers
import sentence_transformers
from transformers import BertTokenizer, BertModel
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
#import os
import joblib
import deep_translator
from deep_translator import GoogleTranslator

import uvicorn
from fastapi import FastAPI



## ggf gar nicht nötig
#modelPath = os.getcwd()
#print(modelPath)


## defining classes and functions 

class model_encoder():
    
    def __init__(self):

        self.model = transf_sen_model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')


    def encode(self, text):

        return self.model.encode(text)




def encode_and_cosine_similarity(text_1: str, text_2: str) -> float:


    encoding_1 = model_enc.encode(text_1)
    encoding_2 = model_enc.encode(text_2)
    
    #assert (str(type(encoding_1))[8:-2] == 'numpy.ndarray') & (str(type(encoding_2))[8:-2] == 'numpy.ndarray')

    return float(cos_sim(encoding_1, encoding_2)[0])



## creating encoder instance 

model_enc = model_encoder()


## defining app  ## 


app = FastAPI()

# Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted flower species with the confidence
@app.post('/predict')
def return_similarity(texts: dict):

    ''' 

    This Fast API App was developed by Nico Schwarzer (https://github.com/NicoSchwarzer/ML_OPS_basic/tree/better_nlp_api).
    It computes the contextual similarity of two texts (which, if need be,
    it translates into English) based on a SOTA Transformer-based Deep Learning method ("https://huggingface.co/sentence-transformers/all-mpnet-base-v2").
    Also, it is hosted on an AWS-EMEA EC-2 instance. 
    
    The API uses a single input parameter in its POST method:
    Text: Dictionary containing two strings between which the contextual similarity is to be inferred - in the form of:
    {"text_1": "This is text_1", "text_2": "This is text_2"}.


    Hence, you can call the URL to this API with the add-on '/predict' (instead of '/docs') and feed in a JSON/Python Dictionary of the form laid out above. 
    Even though this might take some time, one could, for example, call (in Python - using the request library):

    ######

    import requests 


    texts = {'text_1': "i am well", 
    'text_2': "I feel great"}

    (or as an example in 2 different languages):
    texts = {'text_1': "i am well", 
    'text_2': "Ich fühle mich gut"}

    response = requests.post('INSERT_URL/predict', json=texts)
    
    print(response.content)

    ######

    '''
    
    assert str(type(texts)) == "<class 'dict'>"

    text_1 = texts["text_1"]
    text_2 = texts["text_2"]


    # translating into english
    translated_1 = GoogleTranslator(source='auto', target='en').translate(text_1)
    translated_2 = GoogleTranslator(source='auto', target='en').translate(text_2)
    
    sim = encode_and_cosine_similarity(translated_1, translated_2)


    return {
        'The contextual similarity based on a cosine similarity is ': sim
    }





#  Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port=8000)

##@app.get("/items/{item_id}")
##def read_item(item_id: int, q: str, = None):
##    return {"item_id": item_id, "q": q}
