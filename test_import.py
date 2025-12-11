#!/usr/bin/env python
"""
Script para verificar que la aplicación puede iniciarse correctamente
Útil para debugging en Render
"""

import sys
import os
import traceback

# Agregar la raíz del proyecto al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 60)
print("DIAGNÓSTICO DE IMPORTACIÓN")
print("=" * 60)

# Test 1: FastAPI
try:
    print("\n1. Importando FastAPI...")
    from fastapi import FastAPI
    print("   ✓ FastAPI importado correctamente")
except ImportError as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

# Test 2: Configuración
try:
    print("\n2. Importando configuración...")
    from backend.app.core.config import settings
    print(f"   ✓ Configuración cargada")
    print(f"     - DATABASE_URL: {settings.DATABASE_URL[:40]}...")
except Exception as e:
    print(f"   ✗ Error: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test 3: Modelos
try:
    print("\n3. Importando modelos...")
    from backend.app.models.usuario import Usuario
    from backend.app.models.tarea import Tarea
    print("   ✓ Modelos importados correctamente")
except Exception as e:
    print(f"   ✗ Error: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test 4: Schemas
try:
    print("\n4. Importando schemas...")
    from backend.app.schemas.usuario import UsuarioCrear, UsuarioLogin, UsuarioRespuesta
    from backend.app.schemas.tarea import TareaCreate, TareaResponse
    print("   ✓ Schemas importados correctamente")
except Exception as e:
    print(f"   ✗ Error: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test 5: Seguridad
try:
    print("\n5. Importando módulo de seguridad...")
    from backend.app.core.seguridad import encriptar_contraseña, verificar_contraseña
    print("   ✓ Seguridad importada correctamente")
except Exception as e:
    print(f"   ✗ Error: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test 6: Base de datos
try:
    print("\n6. Importando sesión de base de datos...")
    from backend.app.db.session import get_db, engine
    print("   ✓ Sesión de BD importada correctamente")
except Exception as e:
    print(f"   ✗ Error: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test 7: Routers
try:
    print("\n7. Importando routers...")
    from backend.app.api.endpoint.auth import router as auth_router
    from backend.app.api.endpoint.tarea import router as tarea_router
    print("   ✓ Routers importados correctamente")
except Exception as e:
    print(f"   ✗ Error: {e}")
    traceback.print_exc()
    print("   ⚠️  Los routers pueden no estar disponibles")

# Test 8: Aplicación principal
try:
    print("\n8. Importando aplicación principal...")
    from backend.app.main import app
    print("   ✓ Aplicación importada correctamente")
    assert isinstance(app, FastAPI)
    print("   ✓ La aplicación es una instancia válida de FastAPI")
except Exception as e:
    print(f"   ✗ Error: {e}")
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ TODO ESTÁ CORRECTO - La aplicación puede iniciarse")
print("=" * 60)
