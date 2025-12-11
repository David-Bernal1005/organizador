#!/usr/bin/env bash
# start.sh - Script para iniciar la aplicación en Render

echo "========================================="
echo "Iniciando API Organizador de Tareas"
echo "========================================="
echo ""
echo "HOST: 0.0.0.0"
echo "PORT: $PORT"
echo "Module: backend.app.main"
echo ""

# Iniciar uvicorn
python -m uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT --workers 1
