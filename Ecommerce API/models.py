from sqlalchemy import Column, Integer, String, Text
from database import Base

class API(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, nullable=False)
    discounted_price = Column(String, nullable=True)
    Product_image = Column(String, nullable=True)
    Description = Column(String, nullable=True)
    Original_price = Column(String, nullable=True)
    item_number = Column(String, nullable=True)
    attribute_dic = Column(Text, nullable=True)
