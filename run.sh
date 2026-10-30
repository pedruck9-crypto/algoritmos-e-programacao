#!/bin/bash
set -e
cd -- "$(dirname -- "$0")"
echo "Interface: http://127.0.0.1:8000"
echo "Documentação: http://127.0.0.1:8000/docs"
exec python -m uvicorn crud_filmes_e_series:app --reload
