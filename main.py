from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
import pandas as pd
import json
from preprocessing import preproces, fitted_model
import csv
from fastapi.responses import StreamingResponse
from io import StringIO

from models import Item, Items,Event, Item_predicted, Items_predicted

app = FastAPI()



# input_json = """
#     {"name": "bmw",
#     "year": 2010,
#     "km_driven": 10000,
#     "fuel": "Petrol",
#     "seller_type": "Individual",
#     "transmission": "Manual",
#     "owner": "First Owner",
#     "mileage": "23.01 kmpl",
#     "engine": "999 CC",
#     "max_power": "67 bhp",
#     "torque": "91Nm@ 4250rpm",
#     "seats": 5.0
# }
# """


@app.post("/predict_item/")
def predict_item(item: Item) -> float:
    d = item.model_dump()
    df = pd.DataFrame([d])
    df = preproces(df)
    print(df)
    model = fitted_model()
    predict = model.predict(df)
    print(predict)
    return int(predict)


@app.post("/predict_items")
def upload(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    df_preprocessed = preproces(df)
    model = fitted_model()
    predict = model.predict(df_preprocessed)
    df['price_predicted'] = predict
    
    d1 = []
    for index, row in df.iterrows():
        row_dict = row.to_dict() 
        d1.append(row_dict)

    json_d1 = json.dumps(d1)
    items_list = [Item.parse_obj(item) for item in d1]

    return items_list


class Items(BaseModel):
    objects: List[Item]

