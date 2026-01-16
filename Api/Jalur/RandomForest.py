from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
import pickle

router = APIRouter()

with open("Model/RF_RekomendasiTanaman_model.pkl", "rb") as f:
    rf_model = pickle.load(f)

class PlantInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@router.post("/predict")
def predict_RandomForest(data: PlantInput):

    fitur = np.array([[
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall,
    ]])

    hasil = rf_model.predict(fitur)[0]

    return {
        "status": "success",
        "model": "RandomForest",
        "prediction": hasil
    }
