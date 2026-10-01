from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

load_dotenv()

engine = create_engine(os.environ["DATABASE_URL"])

with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    print(result.scalar())