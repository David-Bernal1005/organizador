#!/usr/bin/env python
"""
Script para crear las tablas en la base de datos de Railway
Ejecutar: python create_tables.py
"""

from sqlalchemy import text
from backend.app.db.session import engine
from backend.app.db.base import Base

def create_tables():
    """Crea todas las tablas definidas en los modelos"""
    try:
        print("Creando las tablas en la base de datos...")
        Base.metadata.create_all(bind=engine)
        print("✓ Tablas creadas exitosamente!")
        
        # Verificar las tablas creadas
        with engine.connect() as connection:
            result = connection.execute(text("SHOW TABLES"))
            tables = result.fetchall()
            print(f"\nTablas en la base de datos: {len(tables)}")
            for table in tables:
                print(f"  - {table[0]}")
    except Exception as e:
        print(f"✗ Error al crear las tablas: {e}")

if __name__ == "__main__":
    create_tables()
