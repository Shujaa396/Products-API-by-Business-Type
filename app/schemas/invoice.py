from pydantic import BaseModel
from datetime import date

class InvoiceSchema(BaseModel):
    id: int
    invoice_number: str      # ← add this
    customer_name: str
    amount: float
    date: date
    status: str
