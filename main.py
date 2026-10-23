from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_price
from pydantic import BaseModel, Field

app = FastAPI()


class Vehicle(BaseModel):
    year: int
    mileage: float = Field(ge=0)
    condition: Literal["excellent", "good", "fair"]


@app.get("/")
def home():
    return {"message": "Vehicle Price API is running"}


@app.post("/predict")
def predict(vehicle: Vehicle):
    price = predict_price(
        vehicle.year,
        vehicle.mileage,
        vehicle.condition
    )

    return {"predicted_price": price}