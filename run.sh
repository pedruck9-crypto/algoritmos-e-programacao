#!/bin/bash

# Script para iniciar o servidor FastAPI com uvicorn

echo "Iniciando servidor FastAPI..."
echo "Acesse: http://127.0.0.1:8000"
echo "Documentação: http://127.0.0.1:8000/docs"
echo "Pressione CTRL+C para parar o servidor."
echo ""

python -m uvicorn crud_filmes_e_series:app --reload
