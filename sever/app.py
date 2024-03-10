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
    with open("columns.json", "r") as file:
        data = json.load(file)['data_columns']
except FileNotFoundError:
    print({"error": "File not found"})

try:
    global model
    model = joblib.load(r'C:\Users\Sharda Prasad Maurya.LAPTOP-4MVRVONI\Desktop\projects\pro delhi house\sever\delhi_house_price_prediction')
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Model file not found. Please provide the correct file path.")
    
        
@app.post('/get-me-data')
async def hello(items :Item):
    global location
    location = items.location
    global area 
    area = items.area
    global bed
    bed = items.bed
    global bath
    bath = items.bath
    global parking
    parking = items.parking
    global type
    type = items.type 
    
    return {'location':items.location,'area':items.area,'bed':items.bed,'bath':items.parking,'parking':items.parking,'type of house':items.type}


@app.get('/prediction')
def hello():
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

