#!/usr/bin/env python
"""
Script para crear las tablas en la base de datos de Railway
Ejecutar: python create_tables.py
"""

import sys
import time
from sqlalchemy import text, exc
from backend.app.db.session import engine
from backend.app.db.base import Base

def wait_for_db(max_attempts=10, delay=2):
    """Espera a que la base de datos esté disponible"""
    for attempt in range(max_attempts):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print(f"✓ Base de datos disponible")
            return True
        except exc.OperationalError as e:
            if attempt < max_attempts - 1:
                print(f"⏳ Intento {attempt + 1}/{max_attempts}: Esperando base de datos...")
                time.sleep(delay)
            else:
                print(f"✗ No se pudo conectar a la base de datos: {e}")
                return False
    return False

def create_tables():
    """Crea todas las tablas definidas en los modelos"""
    try:
        print("Esperando conexión a la base de datos...")
        if not wait_for_db():
            print("✗ Error: No se pudo conectar a la base de datos")
            return False
            
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
        return True
    except Exception as e:
        print(f"✗ Error al crear las tablas: {e}")
        return False

if __name__ == "__main__":
    success = create_tables()
    sys.exit(0 if success else 1)
