#!/usr/bin/env bash
# build.sh - Script de construcción para Render

set -o errexit

echo "Instalando dependencias Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Intentando crear las tablas en la base de datos..."
python create_tables.py || echo "Aviso: No se pudieron crear las tablas, puede que ya existan"

echo "Build completado!"
