from typing import Optional
from pydantic import BaseModel


class API(BaseModel):

    id: int
    discounted_price: str
    Product_image: str
    Description: str
    Original_price: str
    item_number: str
    attribute_dic: str

    class Config:
        orm_mode = True