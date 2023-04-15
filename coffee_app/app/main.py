from fastapi import FastAPI
from pymongo.cursor import Cursor #tools for iterating in MongoDB
from bson.objectid import ObjectId
from app.models import Coffee
from database import coffees_collection


app= FastAPI()
 
@app.get("/coffees/", response_model=list[Coffee])
def get_coffees():
    coffees: Cursor = coffees_collections.find()
    coffees_models=[]
    for coffee in coffees: 
        coffe['id']= str(coffee['_id'])
        coffees_models.append(coffee)
    return coffees_models

