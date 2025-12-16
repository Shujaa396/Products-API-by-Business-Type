from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Union
from app.schemas.invoice import InvoiceCreate
from app.services.invoice_service import create_invoices
from app.db import get_db
from app.auth import get_current_user
from app.models.user import User

router = APIRouter(tags=["Invoice Management"])

@router.post(
    "/invoice/create",
    summary="Create one or multiple invoices",
    response_description="List of successfully created invoice IDs",
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {
            "description": "Invoices successfully created",
            "content": {
                "application/json": {
                    "example": {
                        "message": "2 invoice(s) created",
                        "invoices": ["INV-1001", "INV-1002"]
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized (Invalid or missing token)",
            "content": {
                "application/json": {
                    "example": {"detail": "Could not validate credentials"}
                }
            }
        },
        422: {
            "description": "Validation Error (Invalid data or stock issue)",
            "content": {
                "application/json": {
                    "example": {"detail": "Tax must be between 0 and 20 percent"}
                }
            }
        }
    }
)
def create_invoice(
    payload: Union[InvoiceCreate, List[InvoiceCreate]],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    **Create Invoice Endpoint**

    - Accepts **single** or **multiple** invoice objects.
    - Requires **JWT token** in `Authorization` header.
    - Validates:
        - Tax percentage (0–20)
        - Quantity > 0
        - Stock availability
    - Supports **offline invoices** (`is_offline=true`) for later sync.

    **Returns:**
    - Number of created invoices
    - Their IDs
    """
    created_ids = create_invoices(db, payload, current_user)
    return {"message": f"{len(created_ids)} invoice(s) created", "invoices": created_ids}
