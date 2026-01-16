from fastapi import APIRouter
from pydantic import BaseModel, Field
import numpy as np
import pickle

router = APIRouter()

# Load model
with open("Model/CB_TanamanPendamping_model.pkl", "rb") as f:
    cb_model = pickle.load(f)

class PlantSupportInput(BaseModel):
    source_node: str = Field(..., alias="Source Node")
    destination_node: str = Field(..., alias="Destination Node")
    source_type: str = Field(..., alias="Source Type")

    class Config:
        populate_by_name = True

@router.post("/predict")
def predict_catboost(data: PlantSupportInput):

    fitur = np.array([[ 
        data.source_node,
        data.destination_node,
        data.source_type
    ]])

    hasil = cb_model.predict(fitur)[0]
    prediction = str(hasil[0])


    return {
        "status": "success",
        "model": "CatBoost",
        "prediction": prediction
    }
