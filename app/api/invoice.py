from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.invoice import InvoiceSchema
from app.models.invoice import Invoice
from app.db import get_db

# Create router instance
router = APIRouter()
@router.post("/invoices/sync")
async def sync_invoices(batch_invoices: List[InvoiceSchema], db: Session = Depends(get_db)):
    results = []

    for invoice in batch_invoices:
        try:
            existing = db.query(Invoice).filter(Invoice.id == invoice.id).first()
            if existing:
                existing.invoice_number = invoice.invoice_number
                existing.customer_name = invoice.customer_name
                existing.amount = invoice.amount
                existing.date = invoice.date
                existing.status = invoice.status
                db.commit()
                results.append({"invoice_id": invoice.id, "status": "updated"})
            else:
                new_invoice = Invoice(
                    id=invoice.id,
                    invoice_number=invoice.invoice_number,
                    customer_name=invoice.customer_name,
                    amount=invoice.amount,
                    date=invoice.date,
                    status=invoice.status
                )
                db.add(new_invoice)
                db.commit()
                results.append({"invoice_id": invoice.id, "status": "success"})
        except Exception as e:
            db.rollback()
            results.append({"invoice_id": invoice.id, "status": "failed", "error": str(e)})

    return {"results": results}
