from backend.app.database import Base, engine
from backend.app import models

# Create all database tables
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")