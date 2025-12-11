#!/usr/bin/env python
"""
Script para verificar que la aplicación puede iniciarse correctamente
Útil para debugging en Render
"""

import sys
import os

# Agregar la raíz del proyecto al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    print("Intentando importar FastAPI...")
    from fastapi import FastAPI
    print("✓ FastAPI importado correctamente")
    
    print("Intentando importar la configuración...")
    from backend.app.core.config import settings
    print(f"✓ Configuración cargada: DATABASE_URL={settings.DATABASE_URL[:50]}...")
    
    print("Intentando importar la aplicación principal...")
    from backend.app.main import app
    print("✓ Aplicación importada correctamente")
    
    print("Verificando que es una aplicación FastAPI...")
    assert isinstance(app, FastAPI)
    print("✓ La aplicación es una instancia válida de FastAPI")
    
    print("\n✅ TODO ESTÁ CORRECTO - La aplicación puede iniciarse\n")
    
except ImportError as e:
    print(f"✗ Error de importación: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
