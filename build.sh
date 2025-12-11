#!/usr/bin/env bash
# build.sh - Script de construcción para Render

set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Crear las tablas en la base de datos (si no existen)
python create_tables.py

# Recolectar archivos estáticos si es necesario
# python manage.py collectstatic --noinput
