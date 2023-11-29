import pickle
from pydantic import BaseModel
from typing import List
from datetime import date
from typing import Tuple
import pandas as pd


class Item(BaseModel):
    name: str
    year: int
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    mileage: str 
    engine: str
    max_power: str
    torque: str
    seats: float

class Item_predicted(BaseModel):
    name: str
    year: int
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    mileage: str 
    engine: str
    max_power: str
    torque: str
    seats: float
    price_predicted: float

class Items_predicted(BaseModel):
    objects: List[Item_predicted]
    
class Items(BaseModel):
    objects: List[Item]

class Event(BaseModel):
    # model_config = ConfigDict(strict=True)

    when: date
    where: Tuple[int, int]


