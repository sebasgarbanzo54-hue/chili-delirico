from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

class OrderItem(BaseModel):
    product_id: str
    product_name: str
    size_ml: int
    price_crc: int
    quantity: int = Field(gt=0)

class Customer(BaseModel):
    name: str = Field(min_length=2)
    phone: str = Field(min_length=8)
    email: Optional[str] = None
    address: str = Field(min_length=5)
    city: str = Field(min_length=2)
    notes: Optional[str] = ""

class OrderCreate(BaseModel):
    customer: Customer
    items: List[OrderItem]
    subtotal_crc: int
    total_crc: int
    language: str = "es"

class OrderOut(OrderCreate):
    id: str
    created_at: datetime
