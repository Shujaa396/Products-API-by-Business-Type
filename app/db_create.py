# app/db_create.py (temporary script)
from app.db import engine, Base
from app.models.invoice import Invoice

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
