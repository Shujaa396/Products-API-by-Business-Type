from sqlalchemy import Column, Integer, String, Float, Date
from app.db import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, nullable=False)  # ← must match table
    customer_name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
