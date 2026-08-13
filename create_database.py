from app.database.database import engine
from app.database.models import Base


Base.metadata.create_all(engine)

print("Database created successfully")