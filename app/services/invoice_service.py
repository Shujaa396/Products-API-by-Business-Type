from typing import List, Union
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.invoice import InvoiceCreate
from app.models.invoice import Invoice, InvoiceItem
from app.models.product import Product
import uuid

def is_product_in_stock(db: Session, product_id: int, qty: int) -> bool:
    product = db.query(Product).filter(Product.id == product_id).first()
    return bool(product and product.stock >= qty)

def create_invoices(db: Session, payload: Union[InvoiceCreate, List[InvoiceCreate]], current_user) -> List[str]:
    if not isinstance(payload, list):
        payload = [payload]

    created_ids = []

    for inv in payload:
        # Validate items
        for item in inv.items:
            if not is_product_in_stock(db, item.product_id, item.quantity):
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail=f"Product {item.product_id} is out of stock or insufficient quantity."
                )

        # Create invoice ID
        invoice_id = f"INV-{uuid.uuid4().hex[:6].upper()}"

        new_invoice = Invoice(
            invoice_id=invoice_id,
            customer_id=inv.customer_id,
            tax=inv.tax,
            is_offline=inv.is_offline,
            created_by=current_user.id
        )
        db.add(new_invoice)
        db.flush()  # To get invoice primary key

        # Add invoice items
        for item in inv.items:
            new_item = InvoiceItem(
                invoice_id=new_invoice.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price
            )
            db.add(new_item)

            # Deduct stock
            product = db.query(Product).filter(Product.id == item.product_id).first()
            product.stock -= item.quantity

        created_ids.append(invoice_id)

    db.commit()
    return created_ids
