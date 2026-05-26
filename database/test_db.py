# from sqlalchemy import create_engine

# DB_URL = "postgresql://admin:admin123@localhost:5432/vehicle_db"

# engine = create_engine(DB_URL)

# try:
#     connection = engine.connect()
#     print("Connexion PostgreSQL réussie !")
#     connection.close()

# except Exception as e:
#     print("Erreur :", e)

from sqlalchemy import create_engine

DB_URL = "postgresql://admin:admin123@localhost:5432/vehicle_db"
engine = create_engine(DB_URL)

try:
    connection = engine.connect()
    print("Connexion PostgreSQL réussie !")
    connection.close()
except Exception as e:
    print("--- UNE ERREUR EST SURVENUE ---")
    # On force l'extraction du message d'erreur original en ignorant l'erreur d'accent
    error_message = str(e).encode('utf-8', errors='ignore').decode('utf-8')
    print(error_message)
