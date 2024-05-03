from fastapi import FastAPI
import json
import joblib
import numpy as np
from pydantic import BaseModel


class Item(BaseModel):
    location: str
    area: int
    bed: int
    bath: int
    parking: int
    type: int
    

app = FastAPI()

try:
    with open(r"columns.json", "r") as file:
        data = json.load(file)['data_columns']
except FileNotFoundError:
    print({"error": "File not found"})

try:
    global model
    model = joblib.load(r'delhi_house_price_prediction')
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Model file not found. Please provide the correct file path.")
    
        
@app.post('/prediction')
async def hello(items :Item):
    location = items.location
    area = items.area
    bed = items.bed
    bath = items.bath
    parking = items.parking
    type = items.type 
    
    try:
        ind = data.index(location)
    except:
        ind = -1
        
    x = np.zeros(len(data))
    x[0]= area
    x[1]= bed
    x[2]= bath
    x[3]= parking
    x[4]= type
    if ind>4:
        x[ind] = 1
    
    return model.predict([x])[0]
