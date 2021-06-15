from typing import Optional
import joblib
from fastapi import FastAPI
import numpy as np
import json


app = FastAPI()

rf_model = joblib.load(open('/home/arun/Documents/mlwebapp/models/rf.pkl', 'rb'))
@app.get("/test")
def read_root():
    return {"different": "World"}



@app.get("/testing/{item_id}/{secnd}")
async def read_item(item_id,secnd):

    #topred = np.array(list(item_id), dtype=int)
    topred = np.array(json.loads(item_id))
    model = secnd
    print('model',model)
    
    if secnd == "DEEPCNN":
        pred = rf_model.predict(topred)
        prediction  =  "Predicted label - {}".format(model) + " = " + str(pred[0])
        print(prediction)
    elif secnd == 'RF':
        pred = rf_model.predict(topred)
        prediction  =  "Predicted label - {}".format(model) + " = " + str(pred[0])
        print(prediction)
    else:
        pred = rf_model.predict(topred)
        prediction  =  "Predicted label - {}".format(model) + " = " + str(pred[0])
        print(prediction)       

    return {"prediction": prediction}

