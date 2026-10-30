# Inicia o FastAPI a partir da pasta deste script.
Push-Location -LiteralPath $PSScriptRoot
try {
    Write-Host "Interface: http://127.0.0.1:8000" -ForegroundColor Green
    Write-Host "Documentação: http://127.0.0.1:8000/docs"
    python -m uvicorn crud_filmes_e_series:app --reload
} finally {
    Pop-Location
}
