from fastapi import FastAPI
from Jalur.CatBoost import router as cb_router
from Jalur.RandomForest import router as rf_router

app = FastAPI(
    title="Plant Support API",
    description="API untuk memprediksi kualitas wine menggunakan CatBoost & RandomForest",
    version="1.0.0"
)

# Register Router
app.include_router(cb_router, prefix="/cb", tags=["CatBoost"])
app.include_router(rf_router, prefix="/rf", tags=["RandomForest"])
