from fastapi import FastAPI
from app.api import invoice  # add auth if you have

app = FastAPI()

# Include router with prefix
app.include_router(invoice.router, prefix="/api")
