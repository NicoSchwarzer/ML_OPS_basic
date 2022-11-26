# 1. Library imports
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib
import os


# for loading in iris 
#cwd = os.getcwd()

# 2. Class which describes a single flower measurements
class IrisSpecies(BaseModel):
    sepal_length: float 
    sepal_width: float 
    petal_length: float 
    petal_width: float


# 3. Class for training the model and making predictions
class IrisModel:
    # 6. Class constructor, loads the dataset and loads the model
    #    if exists. If not, calls the _train_model method and 
    #    saves the model
    def __init__(self):
        self.df = pd.read_csv('iris.csv')
        self.model_fname_ = 'iris_model.pkl'
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)
        

    # 4. Perform model training using the RandomForest classifier
    def _train_model(self):
        X = self.df.drop('species', axis=1)
        y = self.df['species']
        rfc = RandomForestClassifier()
        model = rfc.fit(X, y)
        return model


    # 5. Make a prediction based on the user-entered data
    #    Returns the predicted species with its respective probability
    def predict_species(self, sepal_length, sepal_width, petal_length, petal_width):
        data_in = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = self.model.predict(data_in)
        probability = self.model.predict_proba(data_in).max()
        return prediction[0], probability




# 1. Library imports
import uvicorn
from fastapi import FastAPI

#try:
#from Model import IrisModel, IrisSpecies ## evtl das hier nicht importieren, sondern den Code in einem File haben!
#except:
#    pass


# 2. Create app and model objects

app = FastAPI()
model = IrisModel()

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted flower species with the confidence
@app.post('/predict')
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model.predict_species(
        data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
    )
    return {
        'prediction': prediction,
        'probability': probability
    }


# 4. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
#if __name__ == '__main__':
##    uvicorn.run(app, host='127.0.0.1', port=8000)

##@app.get("/items/{item_id}")
##def read_item(item_id: int, q: str, = None):
##    return {"item_id": item_id, "q": q}
