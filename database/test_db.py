from sqlalchemy import create_engine

DB_URL = "postgresql://admin:admin123@localhost:5432/vehicle_db"

engine = create_engine(DB_URL)

try:
    connection = engine.connect()
    print("Connexion PostgreSQL reussie !")
    connection.close()

except Exception as e:
    print("Erreur :", e)
