from app.database.session import engine

try:
    with engine.connect() as connection:
        print("✅ Connected to PostgreSQL")
except Exception as e:
    print(e)