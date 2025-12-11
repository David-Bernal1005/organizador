#!/usr/bin/env bash
# build.sh - Script de compilación para Vercel
set -e

echo "Instalando dependencias..."
npm ci

echo "Compilando la aplicación..."
npm run build

echo "Build completado exitosamente!"
