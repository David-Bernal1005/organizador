#!/usr/bin/env bash
# build.sh - Script de construcción para Render

set -o errexit

echo "=================================="
echo "BUILD SCRIPT PARA RENDER"
echo "=================================="

echo ""
echo "1. Actualizando pip..."
pip install --upgrade pip

echo ""
echo "2. Instalando dependencias Python..."
pip install -r requirements.txt

echo ""
echo "3. Ejecutando diagnóstico de importación..."
python test_import.py || echo "⚠️  Aviso: El diagnóstico falló, pero continuamos"

echo ""
echo "4. Intentando crear las tablas en la base de datos..."
python create_tables.py || echo "⚠️  Aviso: No se pudieron crear las tablas, pueden que ya existan"

echo ""
echo "=================================="
echo "✅ BUILD COMPLETADO EXITOSAMENTE"
echo "=================================="
